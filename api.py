from flask_restful import Resource, Api
from model.fighter import Fighter
from app import get_app

app = get_app()
api = Api(app)

class Ranking(Resource):
    def get(self):
        fighters = Fighter.query.all()
        return { "rankings": self._format_rankings(fighters) }
    
    def _format_rankings(self, fighters):
        fight_divisions = { fighter.division for fighter in fighters }
        rankings = {
            cur_division: [
                { 
                    "name": fighter.full_name,
                    "ranking": fighter.ranking
                }
                for fighter in fighters if fighter.division == cur_division
            ]
            for cur_division in fight_divisions
        }
        return rankings
        

api.add_resource(Ranking, '/rankings')

if __name__ == '__main__':
    app.run(debug=True)