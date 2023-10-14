__all__ = ["GeoCityRouter"]


class GeoCityRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in "cities":
            return "geocity"
        return "default"

    def db_for_write(self, model, **hints):
        if model._meta.app_label in "cities":
            return "geocity"
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == "geocity":
            return app_label == "cities"
        if app_label == "cities":
            return db == "geocity"
        return True
