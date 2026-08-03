# Expose submodules so `from app.api.v1.routers import auth, citizens` works
from . import auth
from . import citizens

__all__ = ["auth", "citizens"]
