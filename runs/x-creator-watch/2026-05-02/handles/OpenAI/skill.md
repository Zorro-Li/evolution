# Skill Draft: Official AI Launch Watcher

Use this skill when tracking official AI lab or product accounts such as `@OpenAI`, `@ChatGPTapp`, `@OpenAIDevs`, frontier lab founders, or developer-platform accounts.

## Inputs

- X handle
- visible profile metadata
- recent visible posts
- linked product pages or event pages
- engagement metrics when visible

## Workflow

1. Capture the profile header: bio, website, follower count, join date, and account role.
2. Capture the first visible post batch from Safari / Computer Use.
3. Normalize each post into:
   - date label
   - source URL
   - product or event
   - concrete user action
   - incentive or reward
   - adoption proof
   - linked surface
4. Cluster posts by product push, event push, hiring push, ecosystem retweet, and customer proof.
5. Extract the operating signal:
   - what the lab wants users to do now
   - what product surface is being prioritized
   - what public proof-of-work loop is being encouraged
   - what metrics are used to create trust
6. Produce a short report with:
   - current product direction
   - creator/account strength
   - high-signal posts
   - next action for the user

## Output Template

```md
# <Account> Launch Watch

## Current Push
<one paragraph>

## Product Surface
- <surface>: <why it matters>

## Concrete Actions Asked
- <action>

## Incentive Loop
- <reward or submission mechanic>

## Adoption Proof
- <metric or social proof>

## User Action
- <what to test, archive, or turn into a workflow>
```

## Failure Modes

- Treating official product marketing as neutral research.
- Missing the concrete user action hidden inside the announcement.
- Overweighting retweets without marking the true source account.
- Capturing only engagement metrics and losing product direction.
