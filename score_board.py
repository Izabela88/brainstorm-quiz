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
    def __init__(self, player: Player = None) -> None:

        if player:
            self.game_level = player.game_level
            self.player_name = player.name
            self.score = player.score
            self.game_time = player.game_time

    def save_score(self) -> None:
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
        best_scores[self.game_level] = self.sort_scores(best_scores[self.game_level])
        self.save_best_scores(best_scores)

    def is_score_qualified(self) -> bool:
        is_qualified = False

        best_scores = self.get_best_scores()

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
        self.save_best_scores(best_scores)
        if is_qualified == False:
            console.print(
                f"[bold yellow1]\nWell...{self.player_name} you did not qualify for best scores board this time.\n"
            )
        else:
            console.print(
                f"[bold yellow1]\nYAY! {self.player_name} you have qualified for best scores board!\n"
            )
        return is_qualified

    def show_best_scores(self) -> None:
        best_scores = self.get_best_scores()
        if not best_scores:
            print("\nThere are no results yet!\n")
        for k, v in best_scores.items():
            score_title = Panel.fit(
                Markdown(f"\n10 {k.upper()} LEVEL BEST SCORES:\n", justify="center"),
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
        with open("best_scores.json", "r") as f:
            try:
                scores = json.load(f)
            except json.decoder.JSONDecodeError:
                scores = {}
        return scores

    @staticmethod
    def save_best_scores(best_scores: dict) -> None:
        with open("best_scores.json", "w") as f:
            json.dump(best_scores, f)

    @staticmethod
    def sort_scores(scores: list) -> list:
        return sorted(
            scores,
            key=lambda i: (i["player_score"], -i["player_game_time"]),
            reverse=True,
        )
