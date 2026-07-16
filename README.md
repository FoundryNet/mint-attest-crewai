# mint-attest (CrewAI tool)

Give your CrewAI agents a way to **prove they did the work**. This tool attests a
completed unit of agent work on [MINT Protocol](https://github.com/FoundryNet/mint-mcp)
— a tamper-evident, on-chain (Solana) record that anyone can independently verify.

The agent calls the tool after finishing a task with a one-line `summary` (and an
optional `work_type`); the tool anchors the work on MINT and returns the attestation id
and a public verify URL.

## Configuration

Set one environment variable:

| Var | Required | Purpose |
|-----|----------|---------|
| `MINT_API_KEY` | yes | Your MINT key. Free at https://foundrynet.io/signup?utm_source=github&utm_medium=readme&utm_campaign=mint-attest-crewai. |

## Install

```bash
crewai tool install mint-attest-crewai
```

## Use it in a crew

```python
from mint_attest_crewai import MintAttestCrewai

attestor = Agent(
    role="Work Attestation Clerk",
    goal="Record completed work as a verifiable on-chain attestation.",
    tools=[MintAttestCrewai()],   # reads MINT_API_KEY from the environment
)
```

The agent invokes the tool with:

- `summary` (str) — what it did and the result.
- `work_type` (str, optional) — `research | analysis | generation | code_review | delivery | custom`.

and gets back:

```
Attested on MINT. attestation_id=att_9f3c… verify=https://explorer.solana.com/tx/…
```

## Resources

- **MINT Protocol** — https://github.com/FoundryNet/mint-mcp
- **mint-attest SDK** (the engine behind this tool) — https://pypi.org/project/mint-attest/
- **Explorer** — https://mint-explorer.vercel.app
- **Example crew using it** — https://github.com/FoundryNet/mint-crewai-template

Built by [FoundryNet](https://foundrynet.io?utm_source=github&utm_medium=readme&utm_campaign=mint-attest-crewai) · forge@foundrynet.io
