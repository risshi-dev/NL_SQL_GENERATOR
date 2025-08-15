from typing import TypedDict
from typing_extensions import Annotated

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_google_genai import ChatGoogleGenerativeAI

class QueryOutput(TypedDict):
    """A structured representation of the generated SQL query."""
    query: Annotated[str, "A syntactically valid SQL query."]


class Gemini():
    def __init__(self, pipeline: object, sql_dialect: str = "MySQL"):
        """
        Initializes the model, prompt template, and the processing chain.
        This is done once for efficiency.
        """

        self.__model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
        self.__pipeline = pipeline
        self.__dialect = sql_dialect
        
        prompt_template =   ChatPromptTemplate.from_template(
                                """You are an expert {dialect} developer. Based ONLY on the following database schema, write a single, executable SQL query that answers the user's question.

                                ### Schema:
                                {schema_context}

                                ### User Question:
                                {user_question}"""
                            )
        
        self.__chain: Runnable = prompt_template | self.__model.with_structured_output(QueryOutput)

    def generate_query(self, user_question: str) -> str:
        """
        Generates a SQL query from a user's question.
        
        This method is now stateless and follows a clear sequence of operations.
        """
        
        schema_context = self.__pipeline.query_schema(user_question)

        response: QueryOutput = self.__chain.invoke({
            "dialect": self.__dialect,
            "schema_context": "\n\n".join(schema_context),
            "user_question": user_question
        })
        
        return response["query"]