import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SangroupHostFormComponent } from './sangroup-host-form.component';

describe('SangroupHostFormComponent', () => {
  let component: SangroupHostFormComponent;
  let fixture: ComponentFixture<SangroupHostFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SangroupHostFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SangroupHostFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
