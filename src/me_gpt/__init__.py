"""ME-GPT: A library for creating AI-powered personality clones using vector databases

This library allows users to create digital "clones" of themselves by storing memories
and personality traits in a local vector database, which can then be used to power
conversations with an AI that mimics their personality.

For more information, please visit:
https://github.com/djm93dev/me_gpt
"""

__version__ = "0.1.5"
__author__ = "Daniel McDonald"
__author_email__ = "daniel@danielmcdonald.dev"
__license__ = "MIT"
__copyright__ = "Copyright 2024 Daniel McDonald"

# Core functionality
from me_gpt.ai import (
    initial_questions,
    more_questions,
    prompt_memory,
    chat_with_clone,
    chat,
    clear_chat_memory,
)

# Database and similarity functions
from me_gpt.db import DB, get_embedding
from me_gpt.similarity import (
    cosine_similarity,
    euclidean_metric,
    derridaean_similarity,
    adams_similarity,
    SVM_ranking_algorithm_sort,
)

# Expose all functions for easy import
__all__ = [
    # Core AI functions
    "initial_questions",
    "more_questions",
    "prompt_memory",
    "chat_with_clone",
    "chat",
    "clear_chat_memory",
    # Database components
    "DB",
    "get_embedding",
    # Similarity metrics
    "cosine_similarity",
    "euclidean_metric",
    "derridaean_similarity",
    "adams_similarity",
    "SVM_ranking_algorithm_sort",
]
