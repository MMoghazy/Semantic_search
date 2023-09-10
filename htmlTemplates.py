css = '''
<style>
    .logo-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .logo {
        width: 150px;
    }
    .divider {
        border-radius: 3px;
        height: 3px;
        background-color: #c34a37;
        margin: 0 20px;
    }

    /* Additional CSS styles */
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
    }
    .chat-message.user {
        background-color: #2b313e;
    }
    .chat-message.bot {
        background-color: #475063;
    }
    .chat-message .avatar {
        width: 20%;
    }
    .chat-message .avatar img {
        max-width: 78px;
        max-height: 78px;
        border-radius: 50%;
        object-fit: cover;
    }
    .chat-message .message {
        width: 80%;
        padding: 0 1.5rem;
        color: #fff;
    }
</style>



}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://img.freepik.com/premium-vector/human-symbol-3d-icon-user-business-symbology-website-profile_593228-130.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''



# Define the URLs for your logos
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Oracle_logo.svg/2560px-Oracle_logo.svg.png"
aiLogoUrl = "https://samagic365.blob.core.windows.net/images/White logo transparent.png"

