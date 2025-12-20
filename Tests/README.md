# Tests

**Automated and Manual Testing Framework**

This directory contains all tests for *Days of Future Past*, ensuring code quality, system integration, and player experience validation.

## 🧪 Philosophy

> **Untested code is broken code.**

In a narrative-technical system like this, tests serve multiple purposes:
1. **Verify technical correctness** — Does the code work?
2. **Validate narrative integration** — Does the story trigger properly?
3. **Ensure player experience** — Is it playable and engaging?

## 📂 Structure

```
/Tests/
  /Unit/                    — Isolated component tests
  /Integration/             — System interaction tests
  /AcceptanceTests/         — User-story validation
  /Performance/             — Benchmarks and profiling
  /Manual/                  — Playtest checklists
```

## 🎯 Test Categories

### 1. Unit Tests

**Location:** `/Tests/Unit/`  
**Framework:** NUnit  
**Execution:** Unity Test Runner (Edit Mode)

**Purpose:** Test individual classes and methods in isolation.

**Example:**
```csharp
[Test]
public void FIELDBit_GenerateID_ReturnsUniqueID()
{
    var bit1 = new HomeBit();
    var bit2 = new HomeBit();
    
    Assert.AreNotEqual(bit1.BitID, bit2.BitID);
}
```

**Run command:**
```bash
Unity -runTests -testPlatform editmode -projectPath .
```

### 2. Integration Tests

**Location:** `/Tests/Integration/`  
**Framework:** NUnit  
**Execution:** Unity Test Runner (Play Mode)

**Purpose:** Test interactions between systems (FIELD + Renderer, Narrative + AR, etc.).

**Example:**
```csharp
[UnityTest]
public IEnumerator DualSpaceTransition_UpdatesAllObjects()
{
    // Setup scene with multiple DualSpaceObjects
    // Trigger space transition
    // Verify all objects update materials correctly
    
    yield return new WaitForSeconds(2.0f);
    
    // Assertions...
}
```

**Run command:**
```bash
Unity -runTests -testPlatform playmode -projectPath .
```

### 3. Acceptance Tests

**Location:** `/Tests/AcceptanceTests/`  
**Framework:** NUnit (with qualitative validation)  
**Execution:** Semi-automated + Manual playthrough

**Purpose:** Validate complete player experience against design goals.

**Key file:** `Episode1_Gates.cs` — See [Episode1_Gates.cs](./AcceptanceTests/Episode1_Gates.cs)

**Run command:**
```bash
Unity -runTests -testPlatform playmode -projectPath .
# + Manual playtest to verify qualitative criteria
```

### 4. Performance Tests

**Location:** `/Tests/Performance/`  
**Framework:** Unity Profiler + custom benchmarks  
**Execution:** Manual profiling sessions

**Purpose:** Ensure game meets performance targets (60 FPS on mobile).

**Metrics:**
- Frame rate (target: 60 FPS)
- Memory usage (target: <2GB on mobile)
- Load times (target: <5 seconds for scene load)
- Battery drain (target: <20% per hour)

### 5. Manual Tests

**Location:** `/Tests/Manual/`  
**Format:** Markdown checklists  
**Execution:** Human playtesting

**Purpose:** Validate subjective experience (atmosphere, emotional impact, usability).

**Example checklist:**
```markdown
# Episode 1 Manual Playtest

## Environment
- [ ] Physical Space feels warm and nostalgic
- [ ] Digital Space feels otherworldly and precise
- [ ] Transition between spaces is smooth

## Narrative
- [ ] Story beats are clear
- [ ] Dialogue feels natural
- [ ] Emotional resonance is present

## Usability
- [ ] Controls are intuitive
- [ ] Tutorial is clear
- [ ] No confusing moments
```

## 🎮 Current Test Status

### Episode 1: Home Base

See [Episode1_Gates.cs](./AcceptanceTests/Episode1_Gates.cs) for comprehensive acceptance criteria.

**Current Status:** Foundation phase — all tests failing (expected)

**Priority order:**
1. Gate 1: Environment Setup
2. Gate 2: FIELD System Integration
3. Gate 3: Dual-Space Rendering
4. Gate 4: Narrative Integration
5. Gate 5: AR Integration
6. Gate 6: Performance & Polish
7. Gate 7: Player Experience

## 🔧 Running Tests

### In Unity Editor

1. Open Unity
2. Navigate to `Window > General > Test Runner`
3. Select `EditMode` or `PlayMode` tab
4. Click `Run All` or select specific tests

### From Command Line

```bash
# Edit Mode (Unit Tests)
Unity -runTests -testPlatform editmode -projectPath . -testResults ./TestResults-EditMode.xml

# Play Mode (Integration + Acceptance Tests)
Unity -runTests -testPlatform playmode -projectPath . -testResults ./TestResults-PlayMode.xml
```

### CI/CD Integration

**Coming soon:** GitHub Actions workflow for automated testing on every commit.

## 📝 Writing Tests

### Test Naming Convention

```csharp
[Test]
public void ComponentName_WhenCondition_ThenExpectedBehavior()
{
    // Arrange
    // Act
    // Assert
}
```

**Example:**
```csharp
[Test]
public void FIELDManager_WhenBitRegistered_ThenAppearsInRegistry()
{
    // Arrange
    var manager = new FIELDManager();
    var bit = new HomeBit();
    
    // Act
    manager.Register(bit);
    
    // Assert
    Assert.IsTrue(manager.IsRegistered(bit.BitID));
}
```

### Unity Test Patterns

**For MonoBehaviour testing:**
```csharp
[UnityTest]
public IEnumerator MyComponent_DoesExpectedBehavior()
{
    // Create GameObject with component
    var go = new GameObject();
    var component = go.AddComponent<MyComponent>();
    
    // Wait for initialization
    yield return null;
    
    // Test behavior
    component.DoSomething();
    
    // Wait for result
    yield return new WaitForSeconds(1.0f);
    
    // Assert
    Assert.AreEqual(expectedValue, component.Result);
    
    // Cleanup
    Object.Destroy(go);
}
```

### Test Data Setup

Use `SetUp` and `TearDown` for common setup:

```csharp
public class MyTestSuite
{
    private GameObject testObject;
    
    [SetUp]
    public void SetUp()
    {
        testObject = new GameObject();
    }
    
    [TearDown]
    public void TearDown()
    {
        Object.Destroy(testObject);
    }
    
    [Test]
    public void MyTest()
    {
        // testObject is available here
    }
}
```

## 🎯 Test Coverage Goals

- **Core Systems (FIELD, DualSpace):** 90%+ coverage
- **Narrative Integration:** 80%+ coverage
- **UI/UX:** 70%+ coverage (+ manual testing)
- **AR Features:** 60%+ coverage (hardware-dependent)

**Check coverage:**
```bash
# Unity Code Coverage package required
# Generate report via Unity Editor: Window > Analysis > Code Coverage
```

## 🚨 Test-Driven Development

When implementing new features:

1. **Write failing test first** (Red)
2. **Implement minimal code to pass** (Green)
3. **Refactor for quality** (Refactor)
4. **Repeat**

**Example:**
```csharp
// 1. Write test (fails initially)
[Test]
public void HomeBit_Contains_ReturnsChildBits()
{
    var home = new HomeBit();
    var space = new SpaceBit();
    home.AddContained(space);
    
    Assert.Contains(space, home.GetContained());
}

// 2. Implement HomeBit.AddContained() and GetContained()

// 3. Refactor if needed

// 4. Move to next test
```

## 🤝 Contributing

When submitting code changes:

1. **Write tests for new features**
2. **Ensure existing tests still pass**
3. **Update acceptance tests if needed**
4. **Document any manual testing required**

See [CONTRIBUTING.md](../Community/CONTRIBUTING.md) for full guidelines.

## 📚 Resources

- [Unity Test Framework](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)
- [NUnit Documentation](https://docs.nunit.org/)
- [Test-Driven Development](https://www.agilealliance.org/glossary/tdd/)

---

*Test with intention. Build with confidence.* ✅
