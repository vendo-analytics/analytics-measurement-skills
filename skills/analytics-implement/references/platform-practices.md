# Platform practices

Apply the relevant practices to the actual framework, installed versions, and routing owner. These are decision rules, not a required application architecture or an SDK implementation.

## Shared rules

- Separate business actions, screen visibility, application lifecycle, persistent traits, and server-confirmed outcomes.
- Reuse the existing composition/service boundary for initialization and routing. Keep destination details out of individual action handlers.
- Preserve the same business event meaning across codebases, with explicit platform bindings and destination mappings.
- Define whether an event represents an attempt or completion. Use authoritative server facts when the business outcome requires them.
- Respect current consent and identity contracts, including anonymous-to-known transitions, account switching, and logout. Do not substitute advertising identifiers for user identity.
- Use documented SDK buffering and retry behavior. Do not add a background service or claim that OS suspension guarantees a final flush.
- Verify required platform permissions and provider disclosures against current official documentation; do not claim that installing analytics automatically makes an app compliant.

## Web: HTML and JavaScript

Prefer real action handlers or stable semantic hooks over selectors tied to visual styling. Install listeners once and remove them when their owning component or page lifecycle ends. Avoid layering another listener onto an existing data-layer or auto-capture path. Distinguish interaction with a form from successful completion.

For page views, inspect full navigation versus client routing, and the SDK's automatic capture. Choose one owner. Don't initialize a browser SDK in a server-rendering environment. Test reloads, back/forward navigation, dynamically inserted content, and failed requests where relevant.

Primary reference: [HTML event handling](https://html.spec.whatwg.org/multipage/webappapis.html#events). Consult the actual framework/router documentation before choosing hooks.

## React and web frameworks

Rendering must remain pure. User actions belong in event handlers or the application's domain action. Effects can synchronize with external systems, but an effect rerun must not be mistaken for a newly completed business action. Use the actual router's committed navigation/visibility semantics for screen views. Clean up subscriptions and account for development remounts without masking genuine duplicate initialization.

For SSR/hydration, establish the client boundary and existing automatic page-view behavior before adding tracking. Test route transitions and repeated renders.

Primary reference: [React: synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects).

## iOS: SwiftUI and UIKit

Inspect the current app/scene, navigation, and service ownership. Keep business events at real action/completion boundaries instead of repeated view evaluation. A view's appearance and a scene becoming active are different observations; define what the requested screen event means. Reuse the selected native SDK's supported initialization and lifecycle integration.

Test navigation, repeated appearances, scene transitions, restart, offline/reconnect, consent, and logout as relevant. Verify current privacy/permission requirements for the chosen data and SDK. A simulator is useful evidence but is not proof of every device-specific capability.

Starting references: [SwiftUI ScenePhase](https://developer.apple.com/documentation/swiftui/scenephase) and [UIKit app lifecycle](https://developer.apple.com/documentation/uikit/managing-your-app-s-life-cycle). Fetch the current platform and SDK guidance before applying exact APIs.

## Android: Compose and Views

Keep business events out of repeated composition. Reuse current service and lifecycle ownership; select effect APIs according to what must restart or clean up. Distinguish a recomposition, an Activity recreation, navigation, and a new user action. Inspect existing SDK lifecycle integration before adding observers.

Test recomposition, rotation/recreation, navigation, process restart, foreground transitions, and offline/reconnect where relevant. Preserve identity and consent across the transitions specified by the plan.

Primary reference: [Android: side effects in Compose](https://developer.android.com/develop/ui/compose/side-effects). For Views, consult the current Activity/Fragment and chosen navigation documentation.

## Flutter

Emit actions through existing handlers or state/domain boundaries, not repeated widget builds. Follow the application's actual router; a `NavigatorObserver` can observe a Navigator, but nested navigators or declarative routers need their own documented integration. Reuse a compatible SDK/plugin without duplicating native and Dart event emission.

Test rebuilds, nested navigation, app lifecycle, restart, identity, consent, and offline/reconnect where relevant.

Primary reference: [Flutter NavigatorObserver](https://api.flutter.dev/flutter/widgets/NavigatorObserver-class.html).

## React Native

Apply React action/render distinctions using the app's actual navigation layer and native SDK setup. App foreground state is not screen visibility. Confirm initialization ownership across JavaScript and native layers, clean up subscriptions, and document actual platform differences.

Test navigation, foreground/background transitions, native initialization, reload/restart, and identity/consent behavior on the relevant platforms.

Primary reference: [React Native AppState](https://reactnative.dev/docs/appstate).

## Other codebases

Find their actual action, state, navigation, and application lifecycle owners. Apply the shared rules and consult current official documentation. Record constraints and missing verification access rather than inventing a framework API or excluding a codebase by default.
