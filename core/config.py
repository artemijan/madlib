import os

__all__ = ["Config"]


class Config:
    MADLIB_ENDPOINT = os.environ.get(
        "MADLIB_ENDPOINT", "https://reminiscent-steady-albertosaurus.glitch.me"
    )
