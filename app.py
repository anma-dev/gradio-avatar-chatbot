# import gradio as gr
# import os
# import base64

# # Initial greeting text and video
# intro_text = "অসমৰ বহুতো অনান্বেষিত, আমোদজনক আৰু সুন্দৰ ঠাই য'ত মানসম্পন্ন সময় কটাব পাৰি জীৱনৰ স্মৃতি। অনুগ্ৰহ কৰি কোনটোৰ বিষয়ে অধিক জানিব বিচাৰে সেইটো নিৰ্বাচন কৰক।"
# intro_video_path = "Intro.mp4"

# # Function to encode video to base64
# def encode_video(video_path):
#     if os.path.exists(video_path):
#         with open(video_path, "rb") as video_file:
#             return base64.b64encode(video_file.read()).decode("utf-8")
#     return ""

# # Encode intro video
# intro_video_base64 = encode_video(intro_video_path)

# # HTML for intro video
# intro_video_html = f"""
# <video width='320' height='240' autoplay loop>
#     <source src="data:video/mp4;base64,{intro_video_base64}" type="video/mp4">
# </video>
# """

# # Define the function that will handle the chatbot logic
# def chatbot(choice):
#     if choice == "Kaziranga":
#         video_path = "../D-ID/Kaziranga.mp4"
#         response = "কাজিৰঙা ভাৰতৰ এখন ৰাষ্ট্ৰীয় উদ্যান আৰু ইউনেস্কোৰ বিশ্ব ঐতিহ্য ক্ষেত্ৰ যি এক শিং থকা গঁড়ৰ লগতে বাঘ, হাতী আৰু পৰিভ্ৰমী চৰাইৰ বাবে বিখ্যাত। কাজিৰঙাত থাকিবলৈ কেইবাটাও ৰিজৰ্ট আছে, সকলো ৰেঞ্জৰ বাজেটত, যিয়ে আপোনাক জংগল ছাফাৰী প্ৰদান কৰিব পাৰে, জীপ আৰু হাতী দুয়োটাতে।"
#     elif choice == "Kamakhya":
#         video_path = "../D-ID/Kamakhya.mp4"
#         response = "ভাৰতৰ অসমৰ মনোমোহা পাহাৰত অৱস্থিত কামাখ্যা মন্দিৰ এক শ্ৰদ্ধাৰ তীৰ্থস্থান আৰু পৰ্যটকৰ বাবে অতি আৱশ্যকীয় স্থান। কামাখ্যা দেৱীৰ প্ৰতি উৎসৰ্গিত এই প্ৰাচীন মন্দিৰত আধ্যাত্মিকতা, আচৰিত স্থাপত্য, ব্ৰহ্মপুত্ৰ নদীৰ প্যানোৰামিক দৃশ্যৰ এক অনন্য মিশ্ৰণেৰে ইয়াক এক মনোমোহা সাংস্কৃতিক আৰু প্ৰাকৃতিক আকৰ্ষণৰ কেন্দ্ৰবিন্দু কৰি তোলা হৈছে। দৰ্শকে মন্দিৰৰ ৰহস্য আৰু মনোমোহাতা বৃদ্ধি কৰা কুটিল উৰ্বৰতা অনুষ্ঠান আৰু স্পন্দনশীল স্থানীয় উৎসৱৰ সাক্ষীও হ’ব পাৰে।";
#     elif choice == "Manas":
#         video_path = "../D-ID/Manas.mp4"
#         response = "ভাৰতৰ চিত্ৰময় অসম অঞ্চলত অৱস্থিত মানস ৰাষ্ট্ৰীয় উদ্যান জৈৱ বৈচিত্ৰ্যৰ ভঁৰাল আৰু ইক’-পৰ্যটকৰ স্বপ্নৰ গন্তব্যস্থান। ইউনেস্কোৰ বিশ্ব ঐতিহ্য ক্ষেত্ৰখনে ৰসাল অৰণ্য আৰু মেৰুকৰণ কৰা মানস নদীৰ এক আচৰিত পটভূমিত স্থাপন কৰা লুভীয়া বংগ বাঘ, ভাৰতীয় গঁড়, আৰু বৈচিত্ৰময় চৰাইৰ প্ৰজাতিৰ লগতে বিভিন্ন ধৰণৰ বন্যপ্ৰাণীৰ গৌৰৱ কৰে। দৰ্শকে উদ্যানখনৰ দৃশ্যপটৰ সৌন্দৰ্য্য আৰু উল্লেখযোগ্য সংৰক্ষণ প্ৰচেষ্টাত নিজকে বিলীন কৰি ৰোমাঞ্চকৰ ছাফাৰী, প্ৰকৃতি ভ্ৰমণ, আৰু নদী ক্ৰুজত অংশগ্ৰহণ কৰিব পাৰে।";
#     else:
#         video_path = "../D-ID/Idle.mp4"
#         response = ""

#     # Convert video to base64 for HTML embedding
#     video_base64 = ""
#     if os.path.exists(video_path):
#         with open(video_path, "rb") as video_file:
#             video_base64 = base64.b64encode(video_file.read()).decode("utf-8")

#     # HTML for video playback
#     video_html = f"""
#     <video width='320' height='240' autoplay loop>
#         <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
#     </video>
#     """

#     return video_html, response

# # Create the Gradio interface
# iface = gr.Interface(
#     fn=chatbot,
#     inputs=gr.Radio(["Kaziranga", "Kamakhya", "Manas"], label="Select a Location"),
#     outputs=[gr.HTML(label="Video"), gr.Textbox(label="Information")],
#     title="Assam Tourism Chatbot",
#     description=intro_text,
#     layout="vertical"
# )

# # Add intro video to the interface
# iface.launch()






# import gradio as gr
# import os
# import base64

# # Function to encode video to base64
# def encode_video(video_path):
#     if os.path.exists(video_path):
#         with open(video_path, "rb") as video_file:
#             return base64.b64encode(video_file.read()).decode("utf-8")
#     return ""

# # Encode intro and idle videos
# intro_video_base64 = encode_video("../D-ID/Intro.mp4")
# idle_video_base64 = encode_video("../D-ID/Idle.mp4")

# # HTML for intro video
# intro_video_html = f"""
# <div>
#     <video width='320' height='240' autoplay>
#         <source src="data:video/mp4;base64,{intro_video_base64}" type="video/mp4">
#     </video>
#     <p>অসমৰ বহুতো অনান্বেষিত, আমোদজনক আৰু সুন্দৰ ঠাই য'ত মানসম্পন্ন সময় কটাব পাৰি জীৱনৰ স্মৃতি। অনুগ্ৰহ কৰি কোনটোৰ বিষয়ে অধিক জানিব বিচাৰে সেইটো নিৰ্বাচন কৰক।</p>
# </div>
# """

# # Define the function that will handle the chatbot logic
# def chatbot(choice):
#     video_path = f"../D-ID/{choice}.mp4" if choice in ["Kaziranga", "Kamakhya", "Manas"] else "Idle.mp4"
#     video_base64 = encode_video(video_path)

#     # Set autoplay and loop based on the video
#     autoplay = "autoplay" if choice != "Idle" else ""
#     loop = "loop" if choice == "Idle" else ""

#     # HTML for video playback
#     video_html = f"""
#     <video width='320' height='240' {autoplay} {loop}>
#         <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
#     </video>
#     """

#     # Response text based on the choice
#     response = "Response text for " + choice if choice in ["Kaziranga", "Kamakhya", "Manas"] else ""

#     return video_html, response

# # Create the Gradio interface
# iface = gr.Interface(
#     fn=chatbot,
#     inputs=gr.Radio(["Kaziranga", "Kamakhya", "Manas"], label="Select a Location"),
#     outputs=[gr.HTML(label="Video"), gr.Textbox(label="Information")],
#     title="Assam Tourism Chatbot",
#     description=intro_video_html,
#     layout="vertical"
# )

# iface.launch()






import gradio as gr
import os
import base64

# Function to encode video to base64
def encode_video(video_path):
    if os.path.exists(video_path):
        with open(video_path, "rb") as video_file:
            return base64.b64encode(video_file.read()).decode("utf-8")
    return ""

# Encode the intro and idle videos
intro_video_base64 = encode_video("../D-ID/Intro.mp4")
idle_video_base64 = encode_video("../D-ID/Idle.mp4")

# Define the function that will handle the chatbot logic
def chatbot(choice):
    if choice is None:
        # Use intro video for the initial state
        video_base64 = intro_video_base64
        autoplay = "autoplay"
        loop = ""
    else:
        # Selection state with respective video
        video_path = f"../D-ID/{choice}.mp4"
        video_base64 = encode_video(video_path)
        autoplay = "autoplay"
        loop = ""

    # HTML for video playback
    video_html = f"""
    <video id='gradio-video' width='320' height='240' {autoplay} {loop}>
        <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
    </video>
    """

    # Response text based on the choice
    if choice == "Kaziranga":
        response = "কাজিৰঙা ভাৰতৰ এখন ৰাষ্ট্ৰীয় উদ্যান আৰু ইউনেস্কোৰ বিশ্ব ঐতিহ্য ক্ষেত্ৰ যি এক শিং থকা গঁড়ৰ লগতে বাঘ, হাতী আৰু পৰিভ্ৰমী চৰাইৰ বাবে বিখ্যাত। কাজিৰঙাত থাকিবলৈ কেইবাটাও ৰিজৰ্ট আছে, সকলো ৰেঞ্জৰ বাজেটত, যিয়ে আপোনাক জংগল ছাফাৰী প্ৰদান কৰিব পাৰে, জীপ আৰু হাতী দুয়োটাতে।"
    elif choice == "Kamakhya":
        response = "ভাৰতৰ অসমৰ মনোমোহা পাহাৰত অৱস্থিত কামাখ্যা মন্দিৰ এক শ্ৰদ্ধাৰ তীৰ্থস্থান আৰু পৰ্যটকৰ বাবে অতি আৱশ্যকীয় স্থান। কামাখ্যা দেৱীৰ প্ৰতি উৎসৰ্গিত এই প্ৰাচীন মন্দিৰত আধ্যাত্মিকতা, আচৰিত স্থাপত্য, ব্ৰহ্মপুত্ৰ নদীৰ প্যানোৰামিক দৃশ্যৰ এক অনন্য মিশ্ৰণেৰে ইয়াক এক মনোমোহা সাংস্কৃতিক আৰু প্ৰাকৃতিক আকৰ্ষণৰ কেন্দ্ৰবিন্দু কৰি তোলা হৈছে। দৰ্শকে মন্দিৰৰ ৰহস্য আৰু মনোমোহাতা বৃদ্ধি কৰা কুটিল উৰ্বৰতা অনুষ্ঠান আৰু স্পন্দনশীল স্থানীয় উৎসৱৰ সাক্ষীও হ’ব পাৰে।";
    elif choice == "Manas":
        response = "ভাৰতৰ চিত্ৰময় অসম অঞ্চলত অৱস্থিত মানস ৰাষ্ট্ৰীয় উদ্যান জৈৱ বৈচিত্ৰ্যৰ ভঁৰাল আৰু ইক’-পৰ্যটকৰ স্বপ্নৰ গন্তব্যস্থান। ইউনেস্কোৰ বিশ্ব ঐতিহ্য ক্ষেত্ৰখনে ৰসাল অৰণ্য আৰু মেৰুকৰণ কৰা মানস নদীৰ এক আচৰিত পটভূমিত স্থাপন কৰা লুভীয়া বংগ বাঘ, ভাৰতীয় গঁড়, আৰু বৈচিত্ৰময় চৰাইৰ প্ৰজাতিৰ লগতে বিভিন্ন ধৰণৰ বন্যপ্ৰাণীৰ গৌৰৱ কৰে। দৰ্শকে উদ্যানখনৰ দৃশ্যপটৰ সৌন্দৰ্য্য আৰু উল্লেখযোগ্য সংৰক্ষণ প্ৰচেষ্টাত নিজকে বিলীন কৰি ৰোমাঞ্চকৰ ছাফাৰী, প্ৰকৃতি ভ্ৰমণ, আৰু নদী ক্ৰুজত অংশগ্ৰহণ কৰিব পাৰে।";
    else:
        response = ""

    return video_html, response

# Create the Gradio interface
iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Radio(["Kaziranga", "Kamakhya", "Manas"], label="What would you like to know about?", default=None),
    outputs=[gr.HTML(label="Video"), gr.Textbox(label="Information")],
    title="Assam Tourism Chatbot",
    live=True,
    allow_flagging="never",
)

iface.launch()
