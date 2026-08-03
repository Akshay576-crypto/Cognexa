from unittest.mock import MagicMock

from app.services.tool_executer_service import ToolExecutorService


class TestToolExecutorService:

    def setup_method(self):
        self.executor = ToolExecutorService()

    def test_direct_answer(self):
        result = self.executor.execute(
            tool_name="direct_answer",
            arguments={},
        )

        assert result["success"] is True
        assert result["tool"] == "direct_answer"
        assert result["executed"] is False
        assert result["evidence"] is None
        assert result["error"] is None

    def test_retrieval_tool(self):
        mock_tool = MagicMock()

        mock_tool.invoke.return_value = {
            "query": "What is HAC?",
            "results": [
                {
                    "text": "HAC means Helix Adaptive Chunking."
                }
            ],
        }

        self.executor._tools["retrieval_tool"] = mock_tool

        arguments = {
            "question": "What is HAC?",
            "document_id": None,
            "top_k": 5,
        }

        result = self.executor.execute(
            tool_name="retrieval_tool",
            arguments=arguments,
        )

        mock_tool.invoke.assert_called_once_with(arguments)

        assert result["success"] is True
        assert result["tool"] == "retrieval_tool"
        assert result["executed"] is True
        assert result["evidence"] is not None
        assert result["error"] is None

    def test_web_search_tool(self):
        mock_tool = MagicMock()

        mock_tool.invoke.return_value = {
            "query": "EV market growth in India",
            "results": [
                {
                    "title": "Example",
                    "snippet": "Example result",
                    "url": "https://example.com",
                }
            ],
        }

        self.executor._tools["web_search_tool"] = mock_tool

        arguments = {
            "query": "EV market growth in India",
        }

        result = self.executor.execute(
            tool_name="web_search_tool",
            arguments=arguments,
        )

        mock_tool.invoke.assert_called_once_with(arguments)

        assert result["success"] is True
        assert result["tool"] == "web_search_tool"
        assert result["executed"] is True
        assert result["evidence"] is not None
        assert result["error"] is None

    def test_yahoo_finance_tool(self):
        mock_tool = MagicMock()

        mock_tool.invoke.return_value = {
            "symbol": "AAPL",
            "company": "Apple Inc.",
            "market_data": {},
        }

        self.executor._tools["yahoo_finance_tool"] = mock_tool

        arguments = {
            "symbol": "AAPL",
        }

        result = self.executor.execute(
            tool_name="yahoo_finance_tool",
            arguments=arguments,
        )

        mock_tool.invoke.assert_called_once_with(arguments)

        assert result["success"] is True
        assert result["tool"] == "yahoo_finance_tool"
        assert result["executed"] is True
        assert result["evidence"] is not None
        assert result["error"] is None

    def test_unknown_tool(self):
        result = self.executor.execute(
            tool_name="some_fake_tool",
            arguments={},
        )

        assert result["success"] is False
        assert result["tool"] == "some_fake_tool"
        assert result["executed"] is False
        assert result["evidence"] is None
        assert "Unsupported tool" in result["error"]

    def test_tool_execution_error(self):
        mock_tool = MagicMock()

        mock_tool.invoke.side_effect = Exception(
            "Web search failed"
        )

        self.executor._tools["web_search_tool"] = mock_tool

        arguments = {
            "query": "test",
        }

        result = self.executor.execute(
            tool_name="web_search_tool",
            arguments=arguments,
        )

        mock_tool.invoke.assert_called_once_with(arguments)

        assert result["success"] is False
        assert result["tool"] == "web_search_tool"
        assert result["executed"] is True
        assert result["evidence"] is None
        assert result["error"] == "Web search failed"