from handlers.tasks import router as task_router
from handlers.ping import router as ping_router
from handlers.categories import router as category_router

routers = [task_router, ping_router, category_router]
