# Odoo Debugging

## Golden Rule

Do not patch symptoms before identifying the root cause.

## Debugging Process

### 1. Reproduce

Clearly define:
- expected result
- actual result
- exact user action
- model/record involved
- state
- relevant values

### 2. Trace

Follow the execution path:

UI → action/button → Python method → ORM → related methods → database

For reports:

UI → report action → report model/context → QWeb → helper methods

For frontend:

UI → OWL template → component → service/RPC → backend

### 3. Search

Search for:
- field names
- method names
- XML IDs
- state values
- error messages
- inherited implementations

### 4. Root Cause

State the actual root cause briefly before fixing.

### 5. Fix

Apply the smallest correct change.

### 6. Regression Check

Verify that the fix does not break:
- other states
- other users
- other records
- create/write behavior
- inherited functionality

## Common Odoo Problems

### Field does not exist
Search the complete inheritance chain and installed custom modules.

### XPath does not match
Inspect the final/original view architecture and use a more stable XPath.

### Wrong workflow state
Search every place where the state field is assigned.

### Computed field is wrong
Check `@api.depends`, stored status, related dependencies, and recomputation.

### Duplicate records
Inspect create methods, automated actions, cron jobs, and constraints.

### Access error
Inspect ACLs, record rules, user groups, and whether the operation legitimately requires elevated rights.

### Singleton error
Check whether the method can receive multiple records.

## Final Debug Report

Return:
- Root cause
- File/method responsible
- Fix applied
- Why the fix is safe
- Verification performed
