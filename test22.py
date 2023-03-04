import streamlit as st
import openai

openai.api_key = "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"

def generate_titles(topic_input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"try to give some title options for the given topic 10 max \n\nTopic: {topic_input} \nsuggested titles :\n",
        temperature=0.85,
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
      temperature=0.70,
      max_tokens=1300,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response2['choices'][0]['text']
def paraphrase(user_text):
    response3 = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"paraphrase this text\n\n:{user_text}\n\n\n\nparaphrased text:\n",
        temperature=0.77,
        max_tokens=804,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    paraphrased=response3['choices'][0].text
    return paraphrased
def summarize_text(summarize_input):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"summarize the given text to 300 word \n\ntext: {summarize_input}\n\nsummarized text:\n",
        temperature=0.57,
        max_tokens=2036,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    summarized=response['choices'][0].text
    return summarized

tools = st.sidebar.selectbox("Select a tool", ("Blog Writer", "Sentence Paraphraser",'Summarize Text'))

if tools == 'Blog Writer':
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

    titleinput = st.text_input("give a title for your blog post:")
    if st.button('generate your blog') and titleinput:
        with st.spinner("Generating blog post..."):
            st.write("Here's your blog post:")
            post=generate_blog_post(titleinput)
            st.write(post)
elif tools=='Sentence Paraphraser':
    user_text = st.text_area(label="Enter Your sentence you want to paraphrase ")
    if st.button('paraphrase your sentence') and user_text:
        with st.spinner("Generating paraphrased text..."):
            st.write("Here's your paraphrased post:")
            post2=paraphrase(user_text)
            st.write(post2)
elif tools=='Summarize Text':
    summarize_input=st.text_area(label='Enter your text to summarize it')
    if st.button('summarize text') and summarize_input:
        with st.spinner('summarizing text please wait a moment'):
            st.write('here is your summarized text:')
            summ_post=summarize_text(summarize_input)
            st.write(summ_post)


