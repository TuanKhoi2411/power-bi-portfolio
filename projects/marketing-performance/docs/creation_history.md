# Creation history and provenance

## Source task

Dashboard-development task: `019f8896-46eb-7fa1-88ac-a344a69e62e5`.

Repository-wide recovered workflow: [`../../../docs/BUILD_PROVENANCE.md`](../../../docs/BUILD_PROVENANCE.md).

## Build sequence recovered from the task

1. Public UCI Bank Marketing data was selected as a separate Marketing entity.
2. The source was refreshed with 41,188 contact rows.
3. The initial combined PBIP was corrected for PBIR page discovery and active-page metadata.
4. Base conversion measures were expanded with MoM, variance, contact-frequency, channel, prior-contact, and display measures.
5. Marketing received a technical month-based calendar because the source lacks a normal full date/year; this limitation was explicitly retained.
6. The Marketing project was split into its own PBIP.
7. Two deep-dive pages were added: Audience Segmentation and Campaign Effectiveness.
8. Deep-dive layouts were varied so Job/Age/Marital and campaign timing/frequency analysis did not duplicate the Overview chart grid.
9. The theme was separated from Sales and Finance using a navy/coral marketing direction.

## Current canonical state

Intermediate task counts belong to earlier combined builds. The current standalone project contains **34 measures**, **3 pages**, and **84 report visuals**. Current TMDL and structural validation take precedence over chat history.
