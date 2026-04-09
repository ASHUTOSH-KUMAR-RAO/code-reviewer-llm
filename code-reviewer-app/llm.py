# =============================================================================
# llm.py — LLM Setup and LCEL Chain Builder
# =============================================================================
# This file is responsible for:
#   1. Initializing the ChatGroq LLM with the correct model and settings
#   2. Building the LCEL chain: PromptTemplate | ChatGroq | StrOutputParser
#   3. Running the chain with the correct input variables
# =============================================================================

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts import PROMPT_MAP, TRANSLATOR_MODES

# Load environment variables from .env file
load_dotenv()


# =============================================================================
# CONSTANTS
# =============================================================================

MODEL_NAME   = "openai/gpt-oss-120b"   # Groq model to use
TEMPERATURE  = 0.2                      # Low temp = more focused, deterministic output
MAX_TOKENS   = 4096                     # Max tokens in response


# =============================================================================
# LLM INITIALIZATION
# =============================================================================

def get_llm() -> ChatGroq:
    """
    Initialize and return the ChatGroq LLM instance.

    Returns:
        ChatGroq: Configured LLM ready to use in a chain.

    Raises:
        ValueError: If GROQ_API_KEY is not found in environment.
    """
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY not found! "
            "Please add it to your .env file."
        )

    return ChatGroq(
        api_key=api_key,
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )


# =============================================================================
# CHAIN RUNNER
# =============================================================================

def run_chain(mode: str, code: str, language: str, target_language: str = None) -> str:
    """
    Build and run the LCEL chain for the selected mode.

    LCEL Chain Structure:
        PromptTemplate | ChatGroq | StrOutputParser

    Args:
        mode           (str): The selected analysis mode (e.g. "Bug Finder").
        code           (str): The user's code to analyze.
        language       (str): The programming language of the code.
        target_language(str): Only required for Code Translator mode.

    Returns:
        str: The AI-generated result as a clean string.

    Raises:
        KeyError   : If the mode is not found in PROMPT_MAP.
        ValueError : If target_language is missing for Translator mode.
    """

    # Step 1 — Get the correct prompt template for the selected mode
    if mode not in PROMPT_MAP:
        raise KeyError(f"Unknown mode: '{mode}'. Please select a valid mode.")

    prompt = PROMPT_MAP[mode]

    # Step 2 — Build the LCEL chain
    # Chain: PromptTemplate → LLM → OutputParser
    llm     = get_llm()
    parser  = StrOutputParser()
    chain   = prompt | llm | parser

    # Step 3 — Prepare input variables
    if mode in TRANSLATOR_MODES:
        # Code Translator needs an extra variable: target_language
        if not target_language:
            raise ValueError(
                "target_language is required for Code Translator mode."
            )
        inputs = {
            "code"            : code,
            "language"        : language,
            "target_language" : target_language,
        }
    else:
        # All other modes only need code and language
        inputs = {
            "code"     : code,
            "language" : language,
        }

    # Step 4 — Run the chain and return the result
    result = chain.invoke(inputs)
    return result
