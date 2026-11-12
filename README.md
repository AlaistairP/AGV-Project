# EEG1001 Model AGV Project

__UPLOAD LATEST PPTX FROM LOCAL VAULT - NOT GDRIVE OR REPO__ 

> Team name: **TBD** | Team number: **A4.B** | Presentation date: **DD/MM/YY (TBD)**

Preliminary design of a model Automated Guided Vehicle (AGV) for EEG1001. This repository holds our team's design work, calculations, sketches and presentation materials.

---

## Table of Contents
- [Project Overview]([[#Project Overview]])
- [Deadlines and Key Dates](#deadlines-and-key-dates)
- [Preliminary Design]([[#Repository Structure]])
- [Components](#components)
- [Dimensioning](#dimensioning)
- [Performance](#performance)
- [Workload Split](#workload-split)
- [Team Working](#team-working)
- [Presentation Details](#presentation-details)
- [Slide Requirements](#slide-requirements)
- [Repository Structure]
- [Resources](#resources)
- [Checklist](#checklist)


---

## Project Overview
The AGV project is a team-based module project. Students are allocated to teams of 3 or 4, and team working is central to the project.

The **Preliminary AGV Design presentation** is worth:
- **10%** of the total project mark
- **6.5%** of the overall module mark

> **Note:** Absent or non-participating students receive **0%** for the presentation.

The presentation evaluates:
- Teamwork
- Each team's initial progress on the model AGV design
- Communication skills
- Self-directed learning

---

## Deadlines and Key Dates

| Date                  | Milestone                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| Early in project      | Team membership and email addresses shared via Loop; arrange initial team contact/meeting by email          |
| End of **Week 9**     | Presentation schedule posted on Loop                                                                        |
| **Weeks 10 - 12**     | Team presentations take place                                                                               |
| Before our slot       | Submit **Google Slides link** and **PDF copy** of slides in advance (exact deadline: **05/11, check Loop**) |
| Our presentation slot | **TBD** (15-minute slot)                                                                                    |

---

## Preliminary Design
Our preliminary design covers three areas:

1. Overall chassis dimensions and outline component layout
2. Drive mechanism and calculations (per the Loop document, *Car Driving and Steering Mechanisms*, pages 5 and 6)
3. Steering mechanism and calculations (per the Loop document, *Car Driving and Steering Mechanisms*, pages 18 and 19)

### Chassis and component layout
- Sketches showing the preliminary overall chassis and component layout
- 2D plan and elevation views only (no 3D/isometric needed)

*Design summary: COMPLETED - 04/11*

### Drive mechanism
- Sketches showing what each variable in the equations refers to on the mechanism (e.g. number of teeth on the spur gear *N<sub>s</sub>*, RPM of the spur gear *n<sub>s</sub>*)
- Step-by-step calculations

*Design summary: COMPLETED 28/10*

### Steering mechanism
- 2D plan-view sketches showing variables such as wheelbase *L*, track *W* and turning angles *δ*
- Step-by-step calculations

*Design summary: COMPLETED 01/11*

---

## Components

| Component                          | Description                                                     | Quantity | Notes                     |
| ---------------------------------- | --------------------------------------------------------------- | -------- | ------------------------- |
| MCU                                | Used to interface the<br>ESP32 with the rest of<br>the hardware | 1        | Must be soldered manually |
| 7.2 Battery                        | Li-Ion 7.2V Rechargeable Battery                                | 1        | ---                       |
| 540 Motor                          | Dedicated Drive Motor                                           | 1        | ---                       |
| Futaba S3003 v6 Servo Motor        | Dedicated Servo Motor                                           | 1        | ---                       |
| Electronize Motor Speed Controller | Prebuilt Module, plug and play                                  | 1        | ---                       |
| TCRT5000L Module                   | Prebuilt Module, plug and play                                  | 1        | Some soldering required   |
| 16 Key - KeyPad                    | Prebuilt Module, plug and play                                  | 1        | ---                       |
| 300 x 200 x 2  Aluminium Sheets    | Must be fabricated to spec                                      | 3        | ---                       |

---

## Dimensioning

| Parameter      | Symbol        | Value | Unit |
| -------------- | ------------- | ----- | ---- |
| Overall length | O<sub>L</sub> | TBD   | mm   |
| Overall width  | O<sub>w</sub> | TBD   | mm   |
| Wheelbase      | *L*           | 150   | mm   |
| Track          | *W*           | 200   | mm   |

*Take care with false precision: quote values to a sensible number of significant figures.*

---

## Performance
*To be completed once the drive and steering calculations are finished.*

| Metric | Value | Notes |
|--------|-------|-------|
| TBD | | |

---

## Workload Split

| Team member | Contribution |
|-------------|--------------|
| Member 1 | Steering |
| Member 2 | Component layout / Chassis |
| Member 3 | Drive |
| Member 4 (if applicable) | Teamwork co-ordination / slide preparation |

*The above is based on the sample slide in the project brief. Update with real names and agreed roles.*

All team members must be present and must contribute to the presentation.

---

## Team Working

### Ground rules
As a team we agree to:
- Collectively agree on workload allocation, responsibilities, roles and expectations
- Agree how to address any problems in team interactions
- Revisit these ground rules on an ongoing basis
- Practise professional, constructive interactions: mutual respect for diversity, and space to listen to contrary views
- Agree our communication methods (phone, social media, meetups etc.): **TBD**

### 8 Core Design Principles of Prosociality
1. Strong team identity and understanding of purpose
2. Fair distribution of contributions and benefits
3. Fair and inclusive decision-making
4. Monitoring of agreed behaviours
5. Graduated responding to helpful and unhelpful behaviour
6. Fast and fair conflict resolution
7. Authority to self-govern
8. Appropriate relations with other people and groups

---

## Presentation Details
- **Slot length:** 15 minutes (8-minute presentation + 7-minute Q&A)
- **Attendance:** all team members must be present and must contribute
- **Q&A:** questions may be collective or individual
- **Turnaround is swift**, so everyone must be present and ready on time
- You only attend your own team's presentation
- **Software:** Google Slides (via DCU Google Suite account)
  - One shared Google Slides file, stored in one nominated team member's Google Drive
  - Submit both a Google Slides link and a PDF copy in advance
  - Present directly from Google Slides in the scheduled slot

---

## Slide Requirements

| Slide | Requirements |
|-------|-------------|
| **Title slide** | Team name, team number, presentation date, team member contribution table |
| **Chassis layout** | Hand (pencil) sketches photographed/scanned, 2D plan and elevation, good contrast |
| **Drive design** | Hand-drawn sketches labelling equation components, plus calculations step by step per pages 5 and 6 of *Car Driving and Steering Mechanisms* |
| **Steering design** | Hand-drawn 2D plan sketches labelling *L*, *W*, *δ* etc., plus calculations step by step per pages 18 and 19 of *Car Driving and Steering Mechanisms* |

**Calculations:** do not handwrite them. Format them properly in Google Slides, including mathematical symbols, Greek characters and sub-/superscripts. Beware of false precision.

---

## Repository Structure
*Suggested layout, adjust to suit the team.*

```
.
├── README.md
├── sketches/          # Scanned/photographed hand sketches
├── calculations/      # Drive and steering calculations
├── slides/            # PDF copy of presentation slides
└── notes/             # Meeting notes, ground rules
```

---

## Resources
- *Car Driving and Steering Mechanisms* (Loop document)
- Team Working Resources (Loop)
- Prosociality explanatory video (Loop)
- Preparing a Presentation (Dublin Region Higher Education Alliance)
- The 4Ps of Giving a Good Presentation (University of Hull)
- Google Slides tutorials (Google Help Centre, YouTube)
- Loop course page: https://loop.dcu.ie/course/view.php?id=62015&section=6#

---

## Checklist
- [ ] Team ground rules agreed
- [ ] Communication methods agreed
- [ ] Roles assigned
- [ ] Chassis sketches (plan and elevation) done
- [ ] Drive sketches and calculations done
- [ ] Steering sketches and calculations done
- [ ] Shared Google Slides deck created
- [ ] Presentation schedule checked on Loop (end of Week 9)
- [ ] Slides link and PDF submitted before our slot
- [ ] Presentation rehearsed (8 minutes)
- [ ] Everyone ready for individual Q&A
