import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

# Load environment variables
load_dotenv()

# Initialize the model with deterministic output (temperature=0)
model = ChatOpenAI(temperature=0)

# Simple output parser
parser = StrOutputParser()

# --- Example 1: Simple Sequential Chain ---
print("--- Example 1: Simple Sequential Chain ---")
# Step 1: Define the PromptTemplate
prompt_simple = PromptTemplate.from_template("Generate five interesting facts about {topic}")

# Step 2: Build the chain
simple_chain = prompt_simple | model | parser

# Step 3: Invoke the chain
topic_input = {"topic": "Cricket"}
result_simple = simple_chain.invoke(topic_input)

print(f"Input Topic: {topic_input['topic']}")
print(f"Output:\n{result_simple}\n")

# --- Example 2: Multi-LLM Sequential Chain (Summarization) ---
print("--- Example 2: Multi-LLM Sequential Chain (Summarization) ---")
# Step 1: Define prompts for detailed report and summary
prompt_report = PromptTemplate.from_template("Generate a detailed report on {topic}")
prompt_summary = PromptTemplate.from_template("Generate a five-pointer summary from the following text:\n\n{text}")

# Step 2: Build the chain
multi_step_chain = prompt_report | model | parser | prompt_summary | model | parser

# Step 3: Invoke the chain
topic_input_multi = {"topic": "Unemployment in India"}
result_multi = multi_step_chain.invoke(topic_input_multi)

print(f"Input Topic: {topic_input_multi['topic']}")
print(f"Output (5-point summary):\n{result_multi}\n")

# --- Example 3: Parallel Chain ---
print("--- Example 3: Parallel Chain ---")
# Step 1: Define prompts for notes and quiz
prompt_notes = PromptTemplate.from_template("Generate short and simple notes from the following text:\n\n{text}")
prompt_quiz = PromptTemplate.from_template("Generate five short question-answers from the following text:\n\n{text}")

# Step 2: Define the parallel chains
parallel_notes_chain = prompt_notes | model | parser
parallel_quiz_chain = prompt_quiz | model | parser

# Step 3: Combine parallel chains into a RunnableParallel
parallel_chain = RunnableParallel(notes=parallel_notes_chain, quiz=parallel_quiz_chain)

# Step 4: Define the merging chain
prompt_merge = PromptTemplate.from_template("Merge the provided notes and quiz into a single document.\n\nNotes:\n{notes}\n\nQuiz:\n{quiz}")
merge_chain = prompt_merge | model | parser

# Step 5: Combine everything into a final chain
final_parallel_chain = parallel_chain | merge_chain

# Step 6: Invoke the final chain
input_text_parallel = "Swachh Bharat Abhiyan (SBA) is a nationwide sanitation campaign..."
result_parallel = final_parallel_chain.invoke({"text": input_text_parallel})

print(f"Output (Merged Notes and Quiz):\n{result_parallel}\n")

# --- Example 4: Conditional Chain ---
print("--- Example 4: Conditional Chain ---")

# Step 1: Define the sentiment classification model with Pydantic
class FeedbackSentiment(BaseModel):
    sentiment: Literal["Positive", "Negative"]

# Step 2: Set up the classification prompt
prompt_classify = PromptTemplate.from_template(
    "Classify the sentiment of the following feedback text into Positive or Negative.\n\nFeedback: {feedback}"
)

# Step 3: Create the sentiment classification chain
parser_pydantic = PydanticOutputParser(pydantic_object=FeedbackSentiment)
classification_chain = prompt_classify | model | parser_pydantic

# Step 4: Define the positive and negative response prompts
prompt_positive_response = PromptTemplate.from_template("You received positive feedback: '{feedback}'. Write an appreciative response.")
prompt_negative_response = PromptTemplate.from_template("You received negative feedback: '{feedback}'. Write a supportive response.")

# Step 5: Set up the conditional branch logic
positive_response_chain = prompt_positive_response | model | parser
negative_response_chain = prompt_negative_response | model | parser

# Step 6: Define the branching chain
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", positive_response_chain),
    (lambda x: x.sentiment == "Negative", negative_response_chain),
    RunnableLambda(lambda x: "Could not determine sentiment.")
)

# Step 7: Combine the classification chain and the branching chain
final_conditional_chain = classification_chain | branch_chain

# Step 8: Invoke the final chain with different feedback
feedback_positive = "This is a wonderful smartphone!"
feedback_negative = "This is a terrible phone, the battery dies quickly."
feedback_neutral = "This phone exists."

# Test with positive feedback
print(f"Feedback: '{feedback_positive}'")
result_positive = final_conditional_chain.invoke({"feedback": feedback_positive})
print(f"Response: {result_positive}")

# Test with negative feedback
print(f"Feedback: '{feedback_negative}'")
result_negative = final_conditional_chain.invoke({"feedback": feedback_negative})
print(f"Response: {result_negative}")

# Test with neutral feedback (no sentiment detected)
print(f"Feedback: '{feedback_neutral}'")
result_neutral = final_conditional_chain.invoke({"feedback": feedback_neutral})
print(f"Response: {result_neutral}")
7