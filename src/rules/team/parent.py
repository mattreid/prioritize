import jira


def check_parent_link(issue: jira.resources.Issue, context: dict, _: bool) -> None:
    if issue.raw["Context"]["Related Issues"]["Parent"] is None:
        context["comments"].append(f"  * Issue is missing the link to its parent.")
