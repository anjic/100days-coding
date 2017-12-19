import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OpendatapacComponent } from './opendatapac.component';

describe('OpendatapacComponent', () => {
  let component: OpendatapacComponent;
  let fixture: ComponentFixture<OpendatapacComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OpendatapacComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OpendatapacComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
