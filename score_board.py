import json
import time
import uuid
from player import Player
from rich.panel import Panel
from rich.console import Console
from rich.markdown import Markdown
from rich import print


console = Console()


class ScoreBoard:
    """ScoreBoard class - player scores"""

    def __init__(self, player: Player = None) -> None:
        """Construct method

        :param player: Game player, defaults to None
        :type player: Player, optional
        """
        if player:
            self.game_level = player.game_level
            self.player_name = player.name
            self.score = player.score
            self.game_time = player.game_time

    def save_score(self) -> None:
        """Build up player score and call function to save this to file"""
        player_score = {
            "id": str(uuid.uuid4()),
            "player_name": self.player_name,
            "player_score": self.score,
            "player_game_time": self.game_time,
        }
        best_scores = self.get_best_scores()
        if self.game_level in best_scores:
            best_scores[self.game_level].append(player_score)
        else:
            best_scores[self.game_level] = [player_score]
        best_scores[self.game_level] = self.sort_scores(
            best_scores[self.game_level]
        )
        self.save_to_file(best_scores)

    def is_score_qualified(self) -> bool:
        """Function determine if player score is good enough to be saved

        :return: True if user qualifies, else False
        :rtype: bool
        """
        is_qualified = False

        best_scores = self.get_best_scores()
        self.save_to_file(best_scores)
        level_scores = best_scores.get(self.game_level, [])
        level_scores_sorted = self.sort_scores(level_scores)
        if level_scores:
            lowest_score = level_scores_sorted[-1]["player_score"]
            highest_time = level_scores_sorted[-1]["player_game_time"]
        if len(level_scores) < 10:
            is_qualified = True
        elif self.score > lowest_score:
            level_scores_sorted.pop()
            is_qualified = True
        elif self.score == lowest_score and self.game_time < highest_time:
            level_scores_sorted.pop()
            is_qualified = True

        best_scores[self.game_level] = level_scores_sorted
        self.save_to_file(best_scores)
        if is_qualified is False:
            console.print(
                f"[yellow1]\nWell...{self.player_name} you did not qualify"
                " for best scores board this time but don't give up!\n"
            )
        else:
            console.print(
                f"[bold yellow1]\nHooray!!! {self.player_name} you have"
                " qualified for best scores board!\n"
            )
        return is_qualified

    def show_best_scores(self) -> None:
        """Display best scores"""
        best_scores = self.get_best_scores()
        if not best_scores:
            console.print("\nTHERE ARE NO RESULTS YET!!\n", style="dark_blue")
        for k, v in best_scores.items():
            score_title = Panel.fit(
                Markdown(
                    f"\n10 {k.upper()} LEVEL BEST SCORES:\n", justify="center"
                ),
                width=60,
                style="bold dark_blue",
            )
            console.print(score_title)
            for idx, i in enumerate(v, 1):
                time_formatted = time.strftime(
                    "%H:%M:%S\n", time.gmtime(i["player_game_time"])
                )
                print(
                    f"{idx}. Name: {i['player_name']} --- Score:"
                    f" {i['player_score']} --- Time: {time_formatted}"
                )

    @staticmethod
    def get_best_scores() -> dict:
        """Load best scores from json file

        :return: Best scores object
        :rtype: dict
        """
        with open("best_scores.json", "r") as f:
            try:
                scores = json.load(f)
            except json.decoder.JSONDecodeError:
                scores = {}
        return scores

    @staticmethod
    def save_to_file(best_scores: dict) -> None:
        """Save best scores to json file

        :param best_scores: [description]
        :type best_scores: dict
        """
        with open("best_scores.json", "w") as f:
            json.dump(best_scores, f)

    @staticmethod
    def sort_scores(scores: list) -> list:
        """Sort players scores by score and game time

        :param scores: Players best scores for one game level
        :type scores: list
        :return: Sorted scores
        :rtype: list
        """
        return sorted(
            scores,
            key=lambda i: (i["player_score"], -i["player_game_time"]),
            reverse=True,
        )
