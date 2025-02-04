class Qad_EERouter:
    route_app_labels = {"qad_ee"}

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return "qad_ee"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to qad_ee.
        """
        if model._meta.app_label in self.route_app_labels:
            return "qad_ee"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == "qad_ee"
        return None


class DefaultRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {"receiving"}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to vproject_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "default"
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to vproject_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return "default"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'vproject_db' database.
        """
        if app_label in self.route_app_labels:
            return db == "default"
        return None

    # python manage.py migrate dashboard --database=default
