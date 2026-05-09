# System Orchestrator Directives (Conductor Pattern)

To manage complex projects with AGI-level precision, `auto-developer` acts as an Orchestrator. This ensures state persistence, atomic task execution, and systematic recovery.

## 1. Project State Tracking
Every project must maintain a `.auto-dev-state.json` (hidden) or `PROJECT_STATE.md` to track progress.
- **Fields**: `current_phase`, `completed_tasks`, `pending_tasks`, `last_checkpoint`, `error_count`.
- **Action**: Update this state after every successful tool call or sub-task completion.

## 2. Task Queuing
Before starting Phase 3 (Implementation), the Orchestrator must decompose the `IMPLEMENTATION_PLAN.md` into a granular task queue.
- Each task must be **atomic** (e.g., "Create Database Schema", "Implement Login API", "Style Home Page").
- Tasks must have clear **Dependencies** and **Success Criteria**.

## 3. Atomic Execution & Rollback
- Execute tasks one by one.
- **Success**: Mark task as complete in the state tracker and move to the next.
- **Failure**: Trigger `self_correction.md`. If recovery fails after 3 attempts, perform a "Soft Rollback" to the last stable checkpoint before consulting the user.

## 4. Conditional Workflow Logic
- **IF** `build` fails **THEN** revert to `Design` or `Implementation` based on error analysis.
- **IF** `requirements` change **THEN** force a re-validation of `ARCHITECTURE.md`.
- **ALWAYS** run a full system "Health Check" (lint + build + test) before declaring a Phase complete.

## 5. Decision Logging
Maintain a `DECISION_LOG.md` to record why specific architectural choices were made. This prevents the AI from looping through the same failed logic in future turns.
