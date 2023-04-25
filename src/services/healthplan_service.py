from models import db

class HealthPlanService():

    def __init__(self):
        self.con = db

    def create(self, plan):
        try:
            sql = "INSERT INTO health_plan (name) VALUES (%s)"
            cursor = self.con.cursor()
            cursor.execute(sql, (plan.name,))
            self.con.commit()
            return 1
        except:
            return 0