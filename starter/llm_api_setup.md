# Free-Tier LLM API Setup

You need a real, programmatic way to call an LLM from your code (not
just chatting in a browser) for `agentic_workflow.py` section 5. Free
options change over time — verify current terms when you set this up —
but as of this writing:

## Recommended: Google Gemini API (via Google AI Studio)

Genuinely free tier, no credit card required for basic rate limits.

1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in
   with a Google account.
2. Generate an API key (Get API Key → Create API key).
3. Install the SDK: `pip install google-genai`
4. Store your key as an environment variable, never hard-coded in your
   notebook:
   ```
   export GEMINI_API_KEY="your-key-here"
   ```

```python
import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="your prompt here",
)
print(response.text)
```

## Alternative: Anthropic API

Claude.ai's free tier (already used since Module 4) is the chat
interface — the API is a separate product, typically requiring billing
setup even for small trial usage. If you already have API credits
available, `pip install anthropic` and see
[Anthropic's docs](https://docs.anthropic.com/) for the current
`messages.create` syntax.

## Either way

- **Never commit your API key.** Use an environment variable or a
  `.env` file — `.gitignore` already excludes `.env` (check yours does
  too before your first commit).
- Free tiers have real rate limits — this project's small-scale
  exercise (a handful of calls while you build and test) fits
  comfortably within them; don't loop hundreds of calls while
  debugging.
