from ..celery_app import celery
from ..services import codegen, validator, diagram


@celery.task
def run_agent(suggestion_id: int) -> dict:
    files = codegen.generate_files({})
    validation = validator.validate(files)
    mermaid = diagram.generate({})
    return {"files": files, "validation": validation, "diagram": mermaid}
