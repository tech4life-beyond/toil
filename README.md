# Tech4Life Open Impact License (TOIL)

**Tech4Life & Beyond LLC**  
**Repository Role:** Canonical Licensing Framework  
**Classification:** Public

---

## 1. Purpose

This repository contains the official **Tech4Life Open Impact License (TOIL)** and the supporting documentation required for:

- licensing and commercialization governance,
- auditability and reproducibility of license versions,
- consistent usage across the Tech4Life ecosystem.

TOIL is designed to enable open public benefit while enforcing structured commercial licensing and royalty alignment.

---

## 2. Canonical Legal Text

**The canonical legal text of TOIL is the file:**

- `LICENSE.md`

The repository README is **explanatory** and does not override the legal text.

If any explanatory documentation conflicts with `LICENSE.md`, the license text prevails.

---

## 3. Versioning and Reproducibility

TOIL is a versioned, auditable license framework.

Rules:

- All changes to the license text require a new semantic version release.
- Automation and external repositories must pin to a tagged release when referencing TOIL.
- The license version in use must be explicitly referenced in product packs and contracts.

**Current release (canonical):** `v1.0.0`

Example pin:

```
https://github.com/tech4life-beyond/toil/tree/v1.0.0
```

---

## 4. Ecosystem Integration

TOIL is a core component of the Tech4Life ecosystem.

Primary related repositories:

- `tlos` — Governance and operating doctrine
- `product-registry` — Canonical product IDs
- `product-creation-pipeline` — Product pack validation rules
- `products` — Published product packs
- `kivai` — Platform reference (schema + SDK)

---

## 5. Commercial Use and Enforcement Notice

TOIL permits open impact usage while restricting unauthorized commercial exploitation.

Commercial manufacturing, distribution, or commercial exploitation of Tech4Life products requires formal agreements under the TOIL framework.

Unauthorized commercial activity may be subject to enforcement actions.

---

## 6. How to Use TOIL

Typical usage patterns:

1. Reference the correct TOIL version tag (example: `v1.0.0`).
2. Include TOIL licensing references inside product packs.
3. Use registry IDs for traceable product identity.
4. Use private governance repositories (`legal-private`, `finance-private`) for royalty agreements and enforcement documentation.

---

## 7. License

This repository is governed by the **Tech4Life Open Impact License (TOIL) v1.0.0**.

See `LICENSE.md`.

---

**End of Document**

