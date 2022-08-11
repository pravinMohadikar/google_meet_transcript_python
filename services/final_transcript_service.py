from bs4 import BeautifulSoup
import os


def final_chat(file_name):
    """
    Use beautiful soup to get author and messages from saved caption in html txt file.
    stored all caption in list.
    This function is used to avoid repetition of messages and saved all transcript in a txt file.
    """
    print("meeting ended, captions refactoring")
    list_chat = list()
    with open(file_name, "rb") as file_data:
        for line in file_data.readlines():
            html_content = line.decode().strip()
            #
            bs4_content = BeautifulSoup(html_content, 'html.parser')
            chatbox_html = bs4_content.find_all("div", class_="TBMuR bj4p3b")
            for chat in chatbox_html:
                temp_dict = dict()
                span_msg = chat.find("div", class_="zs7s8d jxFHg").decode_contents().strip()
                if span_msg:
                    temp_dict["author"] = span_msg
                    author_message = chat.find("div", class_="iTTPOb VbkSUe")
                    if author_message:
                        temp_dict["message"] = author_message.text
                    else:
                        temp_dict["message"] = ""
                    list_chat.append(temp_dict)

    """
    To avoid and handel duplication of messages,
    and stored all messages in final list variable.
    """
    final_chat_msg = list()
    temp_dict = dict()
    count = -1
    for author_chat in list_chat:
        count += 1

        # To handel duplication of author messages which captured multiple times.
        if count >= 2 and author_chat['author'] == list_chat[count - 2].get('author'):

            if list_chat[count - 2].get('message').upper() in author_chat['message'].upper():

                continue
            else:
                temp_dict["message"].append(author_chat["message"])
                continue

        """
        To store messages in list, 
        and when author is different list of messages store in dict.
        """
        if temp_dict.get('author') != author_chat['author']:
            if temp_dict:
                temp_dict["message"] = "".join(temp_dict["message"])
                write_str = f"{temp_dict['author']} : {temp_dict['message']}\n"
                # print(write_str)
                final_chat_msg.append(write_str)
            temp_dict = dict()
            temp_dict['author'] = author_chat['author']
            temp_dict['message'] = [author_chat['message']]
            continue

        # To handel same author have multiple similar messages.
        if temp_dict["message"][-1].upper() == author_chat["message"].upper():
            continue

        # To avoid some same messages contains in new messages of same author.
        elif len(temp_dict["message"][-1]) < len(author_chat["message"]):
            old_upper_message = temp_dict["message"][-1].upper()
            new_upper_message = author_chat["message"].upper()
            if old_upper_message in new_upper_message:
                temp_dict["message"][-1] = author_chat["message"]
            else:
                temp_dict["message"].append(author_chat["message"])

        # If above condition are not matching then avoid duplication of messages with previous one.
        else:
            old_upper_message = temp_dict["message"][-1].upper()
            new_upper_message = author_chat["message"].upper()
            if new_upper_message in old_upper_message:
                continue
            else:
                temp_dict["message"].append(author_chat["message"])

    # Write all final messages with author in a txt file.
    file_path = "./output/"
    chat_file_name = f"CHAT_{file_name}"
    new_file_name = os.path.join(file_path, chat_file_name)
    with open(new_file_name, "w+") as out_file:
        out_file.writelines(final_chat_msg)

    print("caption refactoring done and new chat file saved in output folder")
