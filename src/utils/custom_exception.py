import sys

class CustomException(Exception):
    """Base class for custom exceptions in the travel planner application."""
    def __init__(self, message:str,error_detail:Exception=None):
        
        self.error_message = self.get_detailed_error_message(message,error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message:str,error_detail:Exception)->str:
        """Construct a detailed error message including the original exception details."""
        _,_,exc_tb = sys.exc_info()
        line_number = exc_tb.tb_lineno if exc_tb else "Unknown"
        file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"
        error_message = f"Error occurred in file: {file_name} at line: {line_number} with message: {message}"
        if error_detail:
            error_message += f" | Original error details: {str(error_detail)}"
        return error_message
    
    def __str__(self):
        return self.error_message