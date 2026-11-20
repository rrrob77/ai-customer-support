from dataclasses import dataclass

from pydantic_evals import Case, Dataset
from pydantic_evals.evaluators import Evaluator, EvaluatorContext

from app.ai.decide import decide
from app.ai.schemas import Decision
from evals.golden_emails import GOLDEN_EMAILS


@dataclass
class SectionMatches(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        return ctx.output.section == ctx.expected_output["section"]


@dataclass
class ActionMatches(Evaluator):
    def evaluate(self, ctx: EvaluatorContext) -> bool:
        return ctx.output.action == ctx.expected_output["action"]


def run_pipeline(email: str) -> Decision:
    return decide(email)


dataset = Dataset(
    name="golden-emails",
    cases=[
        Case(
            name=x["name"],
            inputs=x["email"],
            expected_output={"section": x["section"], "action": x["action"]},
        )
        for x in GOLDEN_EMAILS
    ],
    evaluators=[SectionMatches(), ActionMatches()],
)

if __name__ == "__main__":
    report = dataset.evaluate_sync(run_pipeline, max_concurrency=4)
    report.print(include_input=False, include_output=True, include_durations=False)