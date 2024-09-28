from datetime import datetime
import uuid

# Mock databases for demonstration purposes
change_requests_db = {}
change_impacts_db = {}

class ChangeRequest:
    def __init__(self, project_id, description, requested_by):
        self.request_id = str(uuid.uuid4())
        self.project_id = project_id
        self.description = description
        self.status = 'Pending'
        self.requested_by = requested_by
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def to_dict(self):
        return {
            "request_id": self.request_id,
            "project_id": self.project_id,
            "description": self.description,
            "status": self.status,
            "requested_by": self.requested_by,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

class ChangeImpact:
    def __init__(self, request_id, impact_analysis, affected_areas):
        self.impact_id = str(uuid.uuid4())
        self.request_id = request_id
        self.impact_analysis = impact_analysis
        self.affected_areas = affected_areas
        self.created_at = datetime.now()

    def to_dict(self):
        return {
            "impact_id": self.impact_id,
            "request_id": self.request_id,
            "impact_analysis": self.impact_analysis,
            "affected_areas": self.affected_areas,
            "created_at": self.created_at,
        }

# CRUD operations for Change Requests
def create_change_request(project_id, description, requested_by):
    change_request = ChangeRequest(project_id, description, requested_by)
    change_requests_db[change_request.request_id] = change_request
    return change_request.to_dict()

def read_change_request(request_id):
    change_request = change_requests_db.get(request_id)
    return change_request.to_dict() if change_request else None

def update_change_request(request_id, updates):
    change_request = change_requests_db.get(request_id)
    if change_request:
        for key, value in updates.items():
            if hasattr(change_request, key):
                setattr(change_request, key, value)
        change_request.updated_at = datetime.now()
        return change_request.to_dict()
    return None

def delete_change_request(request_id):
    if request_id in change_requests_db:
        del change_requests_db[request_id]
        return True
    return False

# Manage Change Requests
def manage_change_requests(request_id, action):
    change_request = change_requests_db.get(request_id)
    if change_request and action in ['approve', 'reject']:
        change_request.status = action.capitalize()
        return change_request.to_dict()
    return None

# Track Change Impact
def track_change_impact(request_id, impact_analysis, affected_areas):
    if request_id in change_requests_db:
        impact = ChangeImpact(request_id, impact_analysis, affected_areas)
        change_impacts_db[impact.impact_id] = impact
        return impact.to_dict()
    return None

# Get Change Impact by ID
def get_change_impact(impact_id):
    impact = change_impacts_db.get(impact_id)
    return impact.to_dict() if impact else None

# Display Menu
def display_menu():
    print("\nChange Request Management System")
    print("-----------------------------------")
    print("1. Create Change Request")
    print("2. Read Change Request")
    print("3. Update Change Request")
    print("4. Delete Change Request")
    print("5. Manage Change Request (Approve/Reject)")
    print("6. Track Change Impact")
    print("7. Get Change Impact by ID")
    print("8. Exit")

# Main function for the menu-driven interface
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            project_id = int(input("Enter project ID: "))
            description = input("Enter change request description: ")
            requested_by = input("Enter requested by: ")
            request = create_change_request(project_id, description, requested_by)
            print("Created Change Request:", request)

        elif choice == "2":
            request_id = input("Enter request ID: ")
            request = read_change_request(request_id)
            print("Read Change Request:", request)

        elif choice == "3":
            request_id = input("Enter request ID: ")
            updates = {}
            field = input("Enter field to update (description/status/requested_by): ")
            updates[field] = input("Enter new value: ")
            updated_request = update_change_request(request_id, updates)
            print("Updated Change Request:", updated_request)

        elif choice == "4":
            request_id = input("Enter request ID: ")
            deletion_success = delete_change_request(request_id)
            print("Deleted Change Request:", deletion_success)

        elif choice == "5":
            request_id = input("Enter request ID: ")
            action = input("Enter action (approve/reject): ")
            managed_request = manage_change_requests(request_id, action)
            print("Managed Change Request:", managed_request)

        elif choice == "6":
            request_id = input("Enter request ID: ")
            impact_analysis = input("Enter impact analysis: ")
            affected_areas = input("Enter affected areas (comma separated): ").split(',')
            impact = track_change_impact(request_id, impact_analysis, [area.strip() for area in affected_areas])
            print("Tracked Change Impact:", impact)

        elif choice == "7":
            impact_id = input("Enter impact ID: ")
            impact = get_change_impact(impact_id)
            print("Get Change Impact:", impact)

        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the main function
if __name__ == "__main__":
    main()
