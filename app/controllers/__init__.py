def blueprints():
    from .main import bp as main_bp
    from .users_controllers import bp as users_bp
    from .lessons_controllers import bp as lessons_bp
    from .attendances_controllers import bp as attendances_bp

    return [main_bp, users_bp, lessons_bp, attendances_bp]
