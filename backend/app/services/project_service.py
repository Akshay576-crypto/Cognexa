from app.repositories.project_reposetory import ProjectRepository

class ProjectService:

    def __init__(self):
        self.reposetrory = ProjectRepository()

    def create_project(self,user_id,project_name,description,project_type):

        project_id = self.reposetrory.create_project(
            user_id=user_id,
            project_name=project_name,
            description=description,
            project_type=project_type
        )

        return {
            "success": True,
            "message": "Project created successfully.",
            "data": {
                "project_id": project_id
            }
        }

    def get_all_projects(self,user_id):

        project = self.reposetrory.get_all_projects(user_id)

        return {
            "success": True,
            "data": project
        }

    def get_project_by_id(self, project_id, user_id):

        project = self.reposetrory.get_project_by_id(
            project_id,
            user_id
        )

        if not project:
            return {
                "success": False,
                "message": "Project not found."
            }

        return {
            "success": True,
            "data": project
        }

    def update_project(self,project_id,user_id,project_name,description,project_type):

        updated = self.reposetrory.update_project(
        project_id=project_id,
        user_id=user_id,
        project_name=project_name,
        description=description,
        project_type=project_type
    )

        if updated == 0:
            return {
            "success": False,
            "message": "Project not found."
                }

        return {
        "success": True,
        "message": "Project updated successfully."
    }

    

    def delete_project(self, project_id, user_id):

        deleted = self.reposetrory.delete_project(
            project_id,
            user_id
        )

        if deleted == 0:
            return {
                "success": False,
                "message": "Project not found."
            }

        return {
            "success": True,
            "message": "Project deleted successfully."
        }


