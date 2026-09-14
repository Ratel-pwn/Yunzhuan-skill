# React Layer Boundary Reference

Use this reference when a React task is large enough that ownership is unclear.

## Smell To Boundary Map

| Smell | Move toward |
| --- | --- |
| Page repeats safe area, header spacing, or bottom nav padding | `src/app/layout/` |
| Page owns tab swipe gesture thresholds or carousel mechanics | shared tab component or feature tab component |
| Page maps raw API/event payloads into display messages | `features/<domain>/model/` |
| Page owns polling/subscriptions/native bridge calls | `features/<domain>/hooks/` or `services/` |
| Multiple screens duplicate a button, input, sheet, drawer, or card | `components/ui/`, `components/overlays/`, `components/chat/`, or a feature component |
| Static mock arrays live inside presentation components | feature `constants/` or service fixtures |
| Business card variants diverge by page | shared card component with narrow variant/action slots |
| Hidden replaced UI remains in JSX | delete it or guard with named feature flag plus removal plan |

## Preferred Refactor Order

1. Identify current behavior and preserve it.
2. Create the correct directory boundary if missing.
3. Move reusable infrastructure without visual/behavior changes.
4. Update pages to compose the new boundary.
5. Apply the requested product change.
6. Remove obsolete local components and hidden dead UI.
7. Verify build and product surface.
