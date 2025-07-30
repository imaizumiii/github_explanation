from manim import *

class GitHubExplanation(Scene):
    def construct(self):
        # Title
        title = Text("GitHubの説明", font_size=72)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Introduction to GitHub
        intro_text = Text("GitHubは、ソフトウェア開発のためのプラットフォームです。", font_size=36)
        self.play(Write(intro_text))
        self.wait(3)
        self.play(FadeOut(intro_text))

        # Features of GitHub
        features = [
            "バージョン管理",
            "コラボレーション",
            "オープンソースプロジェクト",
            "プルリクエスト",
            "イシュートラッキング"
        ]
        
        feature_texts = VGroup(*[Text(feature, font_size=36) for feature in features]).arrange(DOWN)
        self.play(Write(feature_texts))
        self.wait(4)
        self.play(FadeOut(feature_texts))

        # Conclusion
        conclusion_text = Text("GitHubを使って、あなたのプロジェクトを管理しましょう！", font_size=36)
        self.play(Write(conclusion_text))
        self.wait(3)
        self.play(FadeOut(conclusion_text))