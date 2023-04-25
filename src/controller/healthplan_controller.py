from models import db

class HealthPlanController():

    def create(self, plan):
        try:
            sql = "INSERT INTO health_plan(name) VALUES (%s)"
            cursor = db.cursor()
            cursor.execute(sql, (plan))
            db.commit()
            return True
        except:
            return False