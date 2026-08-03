from app.database.db import get_db_connection


class ProjectRepository:

    def create_project(
        self,
        user_id,
        project_name,
        description,
        project_type
    ):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        INSERT INTO projects
        (user_id, project_name,description, project_type)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                user_id,
                project_name,
                description,
                project_type
            )
        )

        connection.commit()

        project_id = cursor.lastrowid

        cursor.close()
        connection.close()

        return project_id

    def update_project(self,project_id,user_id,project_name,description,project_type):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """UPDATE projects 
        SET project_name = %s,
        description = %s,
        project_type = %s,
        updated_at = CURRENT_TIMESTAMP WHERE project_id = %s AND user_id = %s"""

        cursor.execute(
        query,
        (
            project_name,
            description,
            project_type,
            project_id,
            user_id
        )
        )
        connection.commit()

        updated = cursor.rowcount
        cursor.close()
        connection.close()
        return updated

    def get_all_projects(self, user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
        project_id,
        user_id,
        project_name,
        description,
        project_type,
        status,
        created_at,
        updated_at
        FROM projects
        WHERE user_id = %s
        AND status != 'DELETED'
        ORDER BY created_at DESC
        """

        cursor.execute(query, (user_id,))

        projects = cursor.fetchall()

        cursor.close()
        connection.close()

        return projects

    def get_project_by_id(self, project_id, user_id):

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT
        project_id,
        user_id,
        project_name,
        description,
        project_type,
        status,
        created_at,
        updated_at
        FROM projects
        WHERE project_id = %s
        AND user_id = %s
        AND status != 'DELETED'
        """

        cursor.execute(query, (project_id, user_id))

        project = cursor.fetchone()

        cursor.close()
        connection.close()

        return project

    def delete_project(self, project_id, user_id):

        connection = get_db_connection()
        cursor = connection.cursor()

        query = """
        UPDATE projects SET status = 'DELETED',updated_at =  WHERE 
        project_id = %s AND user_id = %s
        """

        cursor.execute(query, (project_id, user_id))

        connection.commit()

        deleted = cursor.rowcount

        cursor.close()
        connection.close()

        return deleted