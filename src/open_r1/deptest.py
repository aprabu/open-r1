try:
    import torch
    import transformers
    import datasets
    import vllm
    import distilabel
    print("All dependencies imported successfully!")
except ImportError as e:
    print("Import error:", e)