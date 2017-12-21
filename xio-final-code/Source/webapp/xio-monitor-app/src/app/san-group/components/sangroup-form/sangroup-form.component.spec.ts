import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SangroupFormComponent } from './sangroup-form.component';

describe('SangroupFormComponent', () => {
  let component: SangroupFormComponent;
  let fixture: ComponentFixture<SangroupFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SangroupFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SangroupFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  // it('should create', () => {
  //   expect(component).toBeTruthy();
  // });
});
