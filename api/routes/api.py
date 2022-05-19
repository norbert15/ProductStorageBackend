from fastapi import APIRouter

from api.routes import product, category, company, user, auth, role, logging, permission


router = APIRouter()

router.include_router(auth.AuthRouter(), prefix="/auth", tags=['Auth'])
router.include_router(product.ProductRouter(), prefix="/products", tags=['Products'])
router.include_router(category.CategoryRouter(), prefix="/categories", tags=['Categories'])
router.include_router(company.CompanyRouter(), prefix="/companies", tags=['Companies'])
router.include_router(user.UserRouter(), prefix="/users", tags=['Users'])
router.include_router(role.RoleRouter(), prefix="/roles", tags=['Roles'])
router.include_router(logging.LoggingRouter(), prefix="/logging", tags=['Logging'])
router.include_router(permission.PermissionRouter(), prefix="/permission", tags=['Permission'])