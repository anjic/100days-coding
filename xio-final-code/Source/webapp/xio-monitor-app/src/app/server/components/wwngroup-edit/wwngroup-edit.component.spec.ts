import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WwngroupEditComponent } from './wwngroup-edit.component';

describe('WwngroupEditComponent', () => {
  let component: WwngroupEditComponent;
  let fixture: ComponentFixture<WwngroupEditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WwngroupEditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WwngroupEditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
