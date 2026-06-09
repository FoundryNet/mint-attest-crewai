"""mint-attest CrewAI tool.

Attest a completed unit of agent work on MINT Protocol — a tamper-evident, on-chain
(Solana) record that this agent did this work, which anyone can independently verify.

This is a thin wrapper over the mint-attest SDK's tool. The agent calls it after
finishing a task with a one-line `summary` (and optional `work_type`); it anchors the
work on MINT and returns the attestation id + public verify URL. Configuration is via
the environment — set `MINT_API_KEY` (get one free at https://foundrynet.io/signup).
"""
from mint_attest.crewai import MintAttestTool


class MintAttestCrewai(MintAttestTool):
    """Attest completed agent work on MINT Protocol.

    Reads `MINT_API_KEY` from the environment. Inherits the SDK tool's behavior:
      - args: summary (str), work_type (str, optional)
      - returns: "Attested on MINT. attestation_id=… verify=…"
    """
    pass


__all__ = ["MintAttestCrewai", "MintAttestTool"]
