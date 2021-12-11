import json
import uuid


class ScoreBoard:
    def save_score(self, game_level, name, score, game_time):
        player_score = {
            "id": str(uuid.uuid4()),
            "player_name": name,
            "player_score": score,
            "player_game_time": game_time,
        }
        best_scores = self.get_best_scores()
        if game_level in best_scores:
            best_scores[game_level].append(player_score)
        else:
            best_scores[game_level] = [player_score]
        best_scores[game_level] = self.sort_scores(best_scores[game_level])
        self.save_best_scores(best_scores)

    def is_score_qualified(self, game_level, player_score, player_time):
        is_qualified = False

        best_scores = self.get_best_scores()

        level_scores = best_scores.get(game_level, [])
        level_scores_sorted = self.sort_scores(level_scores)
        if level_scores:
            lowest_score = level_scores_sorted[-1]["player_score"]
            highest_time = level_scores_sorted[-1]["player_game_time"]
        if len(level_scores) < 10:
            is_qualified = True
        elif player_score > lowest_score:
            level_scores_sorted.pop()
            is_qualified = True
        elif player_score == lowest_score and player_time < highest_time:
            level_scores_sorted.pop()
            is_qualified = True
        best_scores[game_level] = level_scores_sorted
        self.save_best_scores(best_scores)
        return is_qualified

    @staticmethod
    def get_best_scores():
        with open("best_scores.json", "r") as f:
            try:
                scores = json.load(f)
            except json.decoder.JSONDecodeError:
                scores = {}
        return scores

    @staticmethod
    def save_best_scores(best_scores):
        with open("best_scores.json", "w") as f:
            json.dump(best_scores, f)

    @staticmethod
    def sort_scores(scores):
        return sorted(
            scores,
            key=lambda i: (i["player_score"], -i["player_game_time"]),
            reverse=True,
        )
