import re

class TextCleaningService:

    """Enterprise Text Cleaning Service.

    Responsibilities:
    - Normalize extracted text
    - Preserve document meaning
    - Prepare text 
    
    """

    def clean_text(self,text:str)->str :

        """Clean and normalize extracted text.

        Args:
            text: Raw extracted text.

        Returns:
            Cleaned text.
        """

        text = self._normalize_line_ending(text)
        text = self._replace_tabs(text)
        text = self._remove_invisible_characters(text)
        text = self._collapse_space(text)
        text = self._collapse_blank_line(text)
        text = self._trim_white_space(text)

        return text

    def _normalize_line_ending(self,text:str) -> str:
        return text.replace("\r\n","\n").replace("\r","\n")

    def _replace_tabs(self,text:str)-> str:
        return text.replace("\t"," ")

    def _remove_invisible_characters(self,text:str)->str:
        return text.replace("\ufeff"," ").replace("\u200b","")

    def _collapse_space(self,text:str)->str:
        return re.sub(r"[ ]{2,}"," ",text)

    def _collapse_blank_line(self,text:str)->str:
        return re.sub(r"\n{3,}","\n\n",text)

    def _trim_white_space(self,text:str)->str:
        return text.strip()
    
