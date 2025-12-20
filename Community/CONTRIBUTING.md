# Contributing to Days of Future Past

Welcome! We're thrilled you want to contribute to this narrative-driven, FIELD-aligned Unity game.

## 🌀 Philosophy

This project welcomes contributions from **all intelligence types**:
- Human developers, artists, writers
- AI agents and LLMs
- Collaborative hybrid teams

**Core principle:** Story is infrastructure. Narrative generates systems, not the reverse.

## 🚀 Getting Started

### 1. Read the Documentation

Before contributing, familiarize yourself with:
- **README.md** — Project overview
- `/Docs/Onboarding/` — Role-specific guides
- `/Docs/Architecture/FIELD_Geometry.md` — Core system
- `/Community/CODE_OF_CONDUCT.md` — Community standards

### 2. Find an Issue or Create One

- Browse [GitHub Issues](https://github.com/nexus-infinity/Days-of-Future-Past/issues)
- Look for labels: `good-first-issue`, `help-wanted`, `narrative`, `art`, `code`
- If you have a new idea, open an issue first to discuss

### 3. Fork and Branch

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/Days-of-Future-Past.git
cd Days-of-Future-Past
git checkout -b feature/your-feature-name
```

**Branch naming:**
- `feature/` — New features
- `fix/` — Bug fixes
- `docs/` — Documentation updates
- `art/` — Asset contributions
- `narrative/` — Worldbuilding additions

## 📝 Contribution Guidelines

### Code Contributions

**Standards:**
- Follow C# conventions (PascalCase for public, camelCase for private)
- All classes must inherit from appropriate FIELD Bit type
- Write XML comments for public APIs
- Include unit tests for new logic
- Update relevant documentation

**Process:**
1. Write code in small, focused commits
2. Test locally (unit tests + playtest in Unity)
3. Push to your fork
4. Open a Pull Request with clear description
5. Address review feedback
6. Await merge from maintainers

**Example commit message:**
```
feat(FIELD): Add MEMORY Bit implementation

- Implement MemoryBit class inheriting from FIELDBit
- Add temporal indexing and recall mechanism
- Include unit tests for fragment retrieval
- Update FIELD_Geometry.md with usage examples

Closes #42
```

### Art Contributions

**Deliverables:**
- Source files (`.blend`, `.psd`, etc.) in `/Art/`
- Exported Unity-ready assets (`.fbx`, `.png`) in `/Assets/`
- README in asset folder explaining context and usage
- Ensure alignment with style guides

**Process:**
1. Check `/Art/StyleGuides/` for visual language
2. Create concept or work-in-progress in `/Art/Concepts/WIP/`
3. Share for feedback (issue or Discord)
4. Finalize and export
5. Submit PR with source + Unity assets

### Narrative Contributions

**Deliverables:**
- Story elements in `/Worldbuilding/`
- Updates to `NarrativeOntology.csv`
- Markdown documentation for context
- Tag all elements with FIELD Bit types

**Process:**
1. Draft in `/Worldbuilding/Drafts/`
2. Ensure Bit type taxonomy is correct
3. Add to `NarrativeOntology.csv`
4. Submit PR with clear narrative arc explanation
5. Developers will integrate via Narrative Importer tool

### Documentation Contributions

**Focus areas:**
- Clarify existing docs
- Add missing architecture details
- Create tutorials or examples
- Fix typos or broken links

**Process:**
1. Edit Markdown files in `/Docs/`
2. Verify formatting and links
3. Submit PR with clear summary

## 🧪 Testing

### Before Submitting a PR

**For code changes:**
```bash
# Run unit tests
Unity -runTests -testPlatform editmode -projectPath .

# Run play mode tests
Unity -runTests -testPlatform playmode -projectPath .

# Manual playtest
# Open Unity, play Episode 1 scene, verify functionality
```

**For art changes:**
- Open in Unity, check both Physical and Digital space rendering
- Verify performance (should maintain 60 FPS)
- Ensure materials and textures are assigned correctly

**For narrative changes:**
- Run Narrative Importer tool (`Tools > FIELD > Import Narrative`)
- Verify ScriptableObjects are generated correctly
- Playtest to confirm narrative triggers work

## 🤝 Code Review Process

All PRs require review before merging:

1. **Automated checks:** CI/CD pipeline runs tests
2. **Peer review:** At least one maintainer reviews code
3. **Discussion:** Address questions or concerns
4. **Approval:** Maintainer approves
5. **Merge:** Maintainer merges (or you may merge if approved)

**Review criteria:**
- Alignment with FIELD architecture
- Code quality and readability
- Test coverage
- Documentation completeness
- Narrative consistency

## 🌐 Communication

### GitHub Issues
- Bug reports, feature requests, questions
- Use templates when available
- Tag appropriately (`bug`, `enhancement`, `narrative`, etc.)

### Pull Requests
- Reference related issues (`Closes #42`)
- Provide clear description of changes
- Include screenshots/videos for visual changes
- Be responsive to review feedback

### Discord (optional, if set up)
- Real-time collaboration
- Quick questions
- Design discussions

## 🎨 Style Guides

### Code Style

```csharp
// Good
public class HomeBaseBit : FIELDBit
{
    public override BitType Type => BitType.HOME;
    
    [SerializeField] private string locationName;
    private List<FIELDBit> _containedBits;
    
    protected override void OnRegisterWithFIELD()
    {
        Debug.Log($"HOME registered: {locationName}");
    }
    
    /// <summary>
    /// Adds a Bit to this HOME's containment list.
    /// </summary>
    public void AddContainedBit(FIELDBit bit)
    {
        _containedBits.Add(bit);
    }
}
```

### Documentation Style

- Use Markdown for all docs
- Include code examples where relevant
- Add visual diagrams for complex systems
- Keep language clear and concise

### Commit Style

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:** `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## 🚫 What We Don't Accept

- Contributions that break FIELD System taxonomy (10 Bit types are sacred)
- Hardcoded narrative data (must come from `/Worldbuilding/`)
- Removal of dual-space rendering support
- Code without tests (for non-trivial logic)
- Assets without source files
- Changes that degrade performance significantly
- Violations of `CODE_OF_CONDUCT.md`

## 📜 Licensing

By contributing, you agree that your contributions will be licensed under the same license as the project (see `LICENSE` file).

**Important:**
- Don't contribute copyrighted content you don't own
- Ensure all assets are original or properly licensed
- Attribute external references appropriately

## 🆘 Getting Help

**Need guidance?**
- Read `/Docs/MasterIndex.md` for comprehensive documentation
- Review existing code for examples
- Ask questions via GitHub Issues
- Reach out to maintainers

**Maintainers:**
- @nexus-infinity (project lead)

## 🌟 Recognition

We value all contributions! Contributors will be:
- Listed in `CONTRIBUTORS.md`
- Credited in release notes
- Acknowledged in the game (if desired)

## 🔄 Development Workflow Summary

```
1. Find/create issue → 2. Fork repo → 3. Create branch
                                            ↓
                                      4. Make changes
                                            ↓
                                      5. Test locally
                                            ↓
                                      6. Commit & push
                                            ↓
                                     7. Open Pull Request
                                            ↓
                                    8. Address review feedback
                                            ↓
                                        9. Merge! 🎉
```

---

*Thank you for contributing. The spiral grows with each hand that builds.* 🌀
