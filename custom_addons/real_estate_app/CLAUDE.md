# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

`real_estate_app` is a single Odoo 17 custom addon (learning/reference module) living in
`custom_addons/real_estate_app` inside the larger `17-odoo-dev` git repo (repo root is
`17-odoo-dev`, one level above `custom_addons/`; sibling addons `to_do_list_app` and `id_cards`
live next to this module but are unrelated codebases). There is no `odoo-bin` or `odoo.conf` in
this repo — Odoo itself is installed/run elsewhere, and this module is developed by dropping it
into an Odoo 17 instance's addons path.

Many methods in this module are annotated with `### ADD X ###` / `### N-methodname ###` comments
and contain large blocks of commented-out alternative implementations (e.g. `orm_test`,
`print_env_details`). This is intentional — the module doubles as worked examples of Odoo ORM/API
patterns (search, browse, filtered, mapped, sorted, onchange, constrains, cron, actions, wizards,
reports, website controllers, mail templates). When editing, follow this style: keep new example
code commented and labeled rather than deleting it, unless the user asks to clean it up.

## Running / testing

There is no local Odoo binary in this repo. To run the module you need an Odoo 17 server with this
directory on its `--addons-path`. Typical commands (adjust paths/db name for the actual
environment):

```bash
# Update just this module
python3 odoo-bin -c odoo.conf -d <db_name> -u real_estate_app --stop-after-init

# Run this module's tests only
python3 odoo-bin -c odoo.conf -d <db_name> -u real_estate_app --test-enable --stop-after-init \
  --test-tags /real_estate_app
```

Tests live in `tests/test_property.py` (`TestProperty`, an `odoo.tests.common.TransactionCase`)
and must stay registered in `tests/__init__.py`.

There is no linter/formatter config in this module; match existing style (4-space indent, Odoo
naming conventions) rather than reformatting.

## Architecture

**Manifest**: `__manifest__.py` depends on `base`, `mail`, `website` and lists `data/` files before
`views/`/`wizard/`/`reports/` — keep new data/view files registered there and load security CSV
first, sequences/mail templates/wizards next, reports next, then views.

**Core models** (`models/`):
- `property.py` — the central model (`_name = 'property'`), inherits `mail.thread` +
  `mail.activity.mixin` for chatter/tracking. Has a state machine (`draft` → `pending`/`sold`/
  `closed`) driven by button actions (`draft_action`, `pending_action`, `sold_action`,
  `closed_action`), each of which logs a `property.history` record via
  `create_property_history()` before changing state. `sold_action` also sends the
  `email_template_property_sold` mail template. A `property_seq` `ir.sequence` (prefix `PRO`,
  5-digit padding) fills `ref` on create. `PropertyLine` (`property.line`) is a one2many detail
  line on `property`, snapshotted into `property.history.line` on every state change. Two separate
  `tag` many2many fields exist on `property` (`feature_tag_ids`, `amenity_tag_ids`) — each uses its
  own relation table (`property_feature_tag_rel` / `property_amenity_tag_rel`); don't merge them or
  reuse one relation table for both.
- `owner.py` (`owner`) — one2many to `property.property_ids`, one2many to `res.partner` via
  `res_partner.property_owner`, with a smart-button count field and `action_view_property`.
- `res_partner.py` extends `res.partner` (`_inherit`) adding `property_owner` (m2o to `owner`) and
  `age`.
- `property_history.py` — audit trail models `property.history` / `property.history.line`,
  written only from `Property.create_property_history()`.
- `tag.py` — simple shared tag model used by both m2m fields on `property`.

**Wizard** (`wizard/change_state_wizard.py`): `change.state` `TransientModel`, opened from
`property` via `action_open_change_state_wizard()` (passes `default_property_id` through action
context). `action_confirm` only actually changes state when the property is currently `closed`.

**Controllers** (`controllers/`), all separate `http.Controller` classes wired in
`controllers/__init__.py`:
- `property_api.py` — a plain REST-ish JSON API for `property` (`POST /post/property`,
  `POST /post/property/json`, `PUT /update/property/<id>`, `GET /read/property/<id>`,
  `DELETE /delete/property/<id>`, `GET /read/properties?state=...`). All routes use `auth='none'`
  and `csrf=False` and run as `sudo()` — this is a learning API with no authentication; do not
  assume it's safe to expose as-is.
- `property_create.py` / `property_info_page.py` — public `website=True` controllers backing the
  QWeb templates in `views/property_create_template.xml` and `views/property_info_template.xml`
  (form submission flow: `/property/create` → POST `/property/submit` → redirect
  `/property/success`; listing at `/property/info`).
- `test_api.py` — placeholder/demo endpoint only.

**Views/data**: `views/base_menus.xml` defines the app's menu root that the other view files hook
into; each model generally has its own `views/<model>_views.xml`. `data/sequence.xml` and
`data/mail_template.xml` are referenced by id from `property.py` (`property_seq`,
`email_template_property_sold`) — keep those XML ids in sync with the Python `env.ref()` /
`next_by_code()` calls if you rename them. `reports/property_report.xml` defines the printable
report action/template for `property` (`property_report` action, bound to the `property` form via
`binding_model_id`/`binding_type`, rendering `property_report_template`). The template prints
`name`, `ref`, `post_code`, `bedrooms`, `state`, `is_late`, `diff`, `garden_orientation`,
`create_time`, `next_time`, `owner_id` (name/phone) plus its related `res.partner` records
(`owner_id.partner_ids`), `feature_tag_ids` (own table), and `property_line_ids` (own table).

**Security**: `security/ir.model.access.csv` grants full CRUD to every model with no group
restriction (`group_id` column empty) — this is a learning setup, not a production ACL model.

update @CLAUDE.md file after each major change and keep it up to date.0