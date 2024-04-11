from kavenegar import *

def send_otp_code(phone_number , code ) :
    try :
        api = KavenegarAPI('476D45336A454736343867674A734E416C456D6F7A674E69735A624D76774E726E4C6E52663854733235303D')
        params = {
            'sender' : '' ,
            'receptor' : phone_number,
            'message' : f'تست سامانه پیام کوتاه مکاپارس{code}کد تایید شما'
        }

        response = api.sms_send(params)
        print(response)

    except APIException  as e :
        print(e)

    except HTTPException as e :
        print(e)