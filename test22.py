import streamlit as st
import openai

openai.api_key = "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"

def generate_titles(topic_input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"try to give some title options for the given topic like 3 or 4 max \n\nTopic: {topic_input} \nsuggested titles :\n",
        temperature=0.77,
        max_tokens=804,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    titles = response['choices'][0]['text'].split("\n")

    return titles

def generate_blog_post(title_choice):
    response2 = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"generate a blog post based on the given input \n\ninput: {title_choice} \n\n ",
      temperature=0.57,
      max_tokens=804,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response2['choices'][0]['text']

# Create Streamlit app
st.title("Blog Post Generator")

# Get user topic input
topic_input = st.text_input("Enter your topic:")
if st.button("Generate title") and topic_input:
    with st.spinner("Generating title suggestions..."):
        st.write("Here are some title suggestions for your topic:")
        titles=generate_titles(topic_input)
        for title in titles:
            titledef=st.write(f"- {title}")
        st.write(titledef)

titleinput = st.text_input("Enter a title for your blog post:")
if st.button('generate your blog') and titleinput:
    with st.spinner("Generating blog post..."):
        st.write("Here's your blog post:")
        post=generate_blog_post(titleinput)
        st.write(post)

