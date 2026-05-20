def process_exam(
    exam_duration,
    accomodation_status,
    disconnect_duration,
    login_time,
    is_public_holiday
):
    if exam_duration > 150:
        return "Invalid Exam"
    elif accomodation_status or exam_duration < 120:
        return "Exam Accepted"
    else:
        return "Exam Rejected"